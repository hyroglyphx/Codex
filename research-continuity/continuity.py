#!/usr/bin/env python3
"""RCK v0.1: offline, standard-library validator and searchable manifest."""
import json, math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent

def load(name):
    with (ROOT / name).open(encoding='utf-8') as f:
        return json.load(f)

def validate():
    sources = load('sources.json')['sources']
    entries = load('registry.json')['entries']
    scores = load('assessments.json')['assessments']
    ids = [x['id'] for x in sources + entries + scores]
    assert len(ids) == len(set(ids)), 'Duplicate record IDs'
    src_ids = {x['id'] for x in sources}
    entry_ids = {x['id'] for x in entries}
    for e in entries:
        assert set(e['sources']) <= src_ids, e['id']
        assert set(e['dependencies']) <= entry_ids, e['id']
    for a in scores:
        assert set(a['source_ids']) <= src_ids, a['id']
        c = a['components']
        if c:
            assert all(0 <= c[k] <= 1 for k in ('SC','RI','CC','MR','HR'))
            psi = 100*(.25*c['SC']+.20*c['RI']+.20*c['CC']+.15*c['MR']+.20*c['HR'])
            assert abs(psi-a['psi_s']) < 0.011, (a['id'],psi,a['psi_s'])
            ev=a.get('evidence',{})
            if ev:
                w=10*psi*math.prod(ev[k] for k in ('es','er','eh','ep'))**.25*math.exp(-ev['delta_entropy']/.10)
                print(f"{a['id']}: PSI-S={psi:.4f}, calculated WPS-C={w:.4f}, stored WPS-C={a['wps_c']}")
                if a['wps_c'] is not None:
                    assert abs(w-a['wps_c']) < 0.15, (a['id'],w,a['wps_c'])
    print(f'PASS: {len(sources)} source records, {len(entries)} constructs, {len(scores)} assessments')

def search(query):
    query=query.casefold()
    for filename, key in [('sources.json','sources'),('registry.json','entries'),('assessments.json','assessments')]:
        for record in load(filename)[key]:
            if query in json.dumps(record,ensure_ascii=False).casefold():
                print(filename, record['id'], record.get('name',record.get('title','')))

def coverage():
    manifest=load('sources.json')
    print('Declared source universe:',manifest['universe_status'])
    print('Corpus coverage:',manifest['coverage_percentage'])
    for s in manifest['sources']:
        print(s['id'],s['ingestion_status'])

if __name__=='__main__':
    command=sys.argv[1] if len(sys.argv)>1 else 'validate'
    if command=='validate': validate()
    elif command=='search': search(' '.join(sys.argv[2:]))
    elif command=='coverage': coverage()
    else: raise SystemExit('Usage: continuity.py validate|coverage|search <term>')
