import sys
import os
import unittest
import numpy as np

# Ensure we can import the local sovereign_logic package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sovereign_logic.lattice import SovereignLattice

class TestSovereignLattice(unittest.TestCase):
    def setUp(self):
        """Initialize Alpha (Issuer), Beta (Valid Peer), and Fake (Attacker)."""
        self.alpha = SovereignLattice("Alpha-Node")
        self.beta = SovereignLattice("Beta-Node")
        self.fake = SovereignLattice("Infiltrator")
        
        # Simulate a corrupted/malicious Anchor on the Infiltrator
        self.fake.anchor = "BADDATA-0000-0000-0000-000000000000"

    def test_unitary_handshake_success(self):
        """Verify that two nodes with the same Reihman-Lock achieve 0.0 Delta."""
        expected, wave = self.alpha.issue_challenge()
        solution = self.beta.respond_to_challenge(wave)
        success, delta = self.alpha.verify_resonance(expected, solution)
        
        # LOGIC GATE: Must be True and Delta must be absolute zero
        self.assertTrue(success, "Valid Peer failed the Reihman-Lock handshake.")
        self.assertEqual(delta, 0.0, f"Fidelity Drift detected in valid Peer: {delta}")

    def test_unitary_handshake_rejection(self):
        """Verify that an incorrect Anchor results in absolute Rejection (1.0 Delta)."""
        expected, wave = self.alpha.issue_challenge()
        solution = self.fake.respond_to_challenge(wave)
        success, delta = self.alpha.verify_resonance(expected, solution)
        
        # LOGIC GATE: Must be False and Delta must be 1.0 (Total Decoherence)
        self.assertFalse(success, "Infiltrator successfully bypassed the Anchor!")
        self.assertEqual(delta, 1.0, "Infiltrator did not trigger total decoherence.")

if __name__ == "__main__":
    unittest.main()
