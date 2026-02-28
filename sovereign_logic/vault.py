import json
import os
import numpy as np
from sovereign_logic.lattice import SovereignLattice

class SovereignVault:
    def __init__(self, vault_file="sovereign_vault.json"):
        self.vault_file = vault_file
        self.lattice = SovereignLattice(node_id="Vault-Alpha")
        self.data = self._load_vault()

    def _load_vault(self):
        if os.path.exists(self.vault_file):
            with open(self.vault_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def secure_write(self, key, value, client_wave, client_hash):
        """
        Only accepts writes if the Fidelity Delta is exactly 0.00000000.
        """
        # Challenge the incoming wave
        solution = self.lattice.respond_to_challenge(client_wave)
        success, delta = self.lattice.verify_resonance(client_hash, solution)
        
        if success and delta == 0.0:
            self.data[key] = value
            with open(self.vault_file, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True, delta
        return False, delta

    def secure_read(self, key):
        """
        Standard retrieval from the verified dataset.
        """
        return self.data.get(key, "COHERENCE_MISSING")
