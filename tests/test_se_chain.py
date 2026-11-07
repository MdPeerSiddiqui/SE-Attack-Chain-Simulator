#!/usr/bin/env python3
"""
Unit Tests for PEER'S SE Attack Chain Simulator (Day 15 Capstone)
Sqrock IT Solutions - Cybersecurity Internship Phase 1
"""

import os
import sys
import unittest
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from se_chain_simulator import SEAttackChainSimulator


class TestSEAttackChain(unittest.TestCase):
    """Test suite for full Cyber Kill Chain simulation and SOAR defense containment."""

    def setUp(self):
        self.sim = SEAttackChainSimulator()

    def test_phase1_recon(self):
        """Test Phase 1 passive reconnaissance and employee footprinting."""
        p1 = self.sim.execute_phase1_recon()
        self.assertEqual(p1["status"], "COMPLETED")
        self.assertGreaterEqual(len(p1["enumerated_employees"]), 2)
        self.assertTrue(any(e["email"] == "j.smith@sqrock-solutions.com" for e in p1["enumerated_employees"]))

    def test_phase2_weaponization(self):
        """Test Phase 2 weaponization and targeted lure crafting."""
        p2 = self.sim.execute_phase2_weaponization()
        self.assertEqual(p2["status"], "COMPLETED")
        self.assertIn("sqrock-verify-portal.net", p2["harvesting_url"])
        self.assertEqual(len(p2["tracking_token"]), 10)

    def test_phase3_exploitation(self):
        """Test Phase 3 user execution and credential capture simulation."""
        p3 = self.sim.execute_phase3_exploitation()
        self.assertEqual(p3["status"], "COMPLETED")
        self.assertTrue(p3["victim_clicked"])
        self.assertIn("j.smith@sqrock-solutions.com", p3["harvested_credentials"]["username"])

    def test_phase4_siem_detection(self):
        """Test Phase 4 SIEM ingestion and multi-source threat correlation."""
        p4 = self.sim.execute_phase4_siem_detection()
        self.assertEqual(p4["status"], "COMPLETED")
        self.assertEqual(p4["total_alerts"], 3)
        alert_ids = [a["alert_id"] for a in p4["correlated_alerts"]]
        self.assertIn("ALRT-ATO-j.smith", alert_ids)

    def test_phase5_containment(self):
        """Test Phase 5 automated containment across identity, mailbox, and firewall."""
        p5 = self.sim.execute_phase5_containment()
        self.assertEqual(p5["status"], "COMPLETED")
        self.assertEqual(len(p5["actions_executed"]), 4)
        actions = [a["action"] for a in p5["actions_executed"]]
        self.assertIn("IDENTITY_CONTAINMENT", actions)
        self.assertIn("MAILBOX_CONTAINMENT", actions)
        self.assertIn("NETWORK_PERIMETER_BLOCK", actions)

    def test_full_chain_and_export(self):
        """Test full end-to-end execution of all 5 kill chain phases and JSON/TXT audit export."""
        chain = self.sim.run_entire_chain()
        self.assertEqual(chain["status"], "SIMULATION_SUCCESSFULLY_CONTAINED")
        self.assertEqual(len(chain["phases"]), 5)

        res = self.sim.export_reports()
        self.assertEqual(res["status"], "SIMULATION_SUCCESSFULLY_CONTAINED")

        json_path = os.path.join(BASE_DIR, "simulations", "attack_chain_report.json")
        txt_path = os.path.join(BASE_DIR, "simulations", "attack_chain_summary.txt")
        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(txt_path))


if __name__ == "__main__":
    unittest.main()
