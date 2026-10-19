#!/usr/bin/env python3
"""Offline regression checks for RCK and Reuptake."""
import unittest
import relay_bridge

class BridgeTests(unittest.TestCase):
    def test_events_unique(self):
        events = relay_bridge.read_events()
        self.assertGreater(len(events), 0)
        self.assertEqual(len(events), len(relay_bridge.build_index(events)))

    def test_search_exact_event(self):
        first = relay_bridge.read_events()[0]["event_id"]
        self.assertIn(first, [event["event_id"] for event in relay_bridge.query(first)])

    def test_related_not_identity(self):
        report = relay_bridge.snapshot()
        entry = next(x for x in report["construct_links"] if x["construct_id"] == "ECVR-HETEROGRAM-001")
        self.assertEqual(entry["relation_status"], "related_not_identity")
        self.assertEqual(len(entry["related_events"]), 3)
        self.assertEqual(entry["linked_events"], [])

    def test_coverage_unknown(self):
        self.assertEqual(relay_bridge.snapshot()["coverage_status"], "unknown")

if __name__ == "__main__":
    unittest.main()
