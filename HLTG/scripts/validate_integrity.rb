#!/usr/bin/env ruby
require "yaml"

ROOT = File.expand_path("..", __dir__)
required = %w[
  README.md
  schema/artifact.schema.yaml
  registry/languages.yaml
  registry/relations.yaml
  artifacts
  observations
  processors
  packets
  benchmarks/HISTORICAL_REINFORCEMENT.md
  RESEARCH_INTEGRITY_GATES.md
]

errors = []
required.each do |rel|
  errors << "missing required HLTG path: #{rel}" unless File.exist?(File.join(ROOT, rel))
end

Dir.glob(File.join(ROOT, "**", "*")).select { |p| File.file?(p) }.each do |path|
  text = File.read(path, encoding: "UTF-8")
  if text.match?(/^(<<<<<<<|=======|>>>>>>>)/)
    errors << "merge-conflict marker: #{path.sub(ROOT + "/", "")}"
  end
end

class NoDuplicateKeys < Psych::Handler
  def initialize(path, errors)
    @path, @errors, @stack = path, errors, []
  end
  def start_mapping(*) = @stack << {}
  def end_mapping = @stack.pop
  def scalar(value, *)
    return if @stack.empty?
    frame = @stack.last
    if frame[:expect_value]
      frame[:expect_value] = false
    else
      if frame.key?(value)
        @errors << "duplicate YAML key '#{value}' in #{@path}"
      end
      frame[value] = true
      frame[:expect_value] = true
    end
  end
end

Dir.glob(File.join(ROOT, "**", "*.{yaml,yml}")).sort.each do |path|
  rel = path.sub(ROOT + "/", "")
  begin
    Psych.parse_stream(File.read(path, encoding: "UTF-8"), filename: rel)
    parser = Psych::Parser.new(NoDuplicateKeys.new(rel, errors))
    parser.parse(File.read(path, encoding: "UTF-8"))
  rescue Psych::SyntaxError => e
    errors << "YAML parse error in #{rel}: #{e.message}"
  end
end

if errors.empty?
  puts "HLTG integrity gates: PASS"
  exit 0
else
  warn errors.join("\n")
  exit 1
end
