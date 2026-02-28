import numpy as np
from sovereign_logic.vault import SovereignVault
from sovereign_logic.lattice import SovereignLattice

# Setup
vault = SovereignVault()
lattice = SovereignLattice(node_id="Tester")

# 1. THE SOVEREIGN WRITE (26.829 Hz)
perfect_wave = lattice.generate_unitary_wave()
perfect_hash = lattice.respond_to_challenge(perfect_wave)
success, delta = vault.secure_write("Genesis_Block", "Lattice_Stabilized", perfect_wave, perfect_hash)
print(f"Sovereign Write: {'SUCCESS' if success else 'FAILED'} (Delta: {delta:.8f})")

# 2. THE NOISE ATTACK (Random Data)
noise_wave = np.random.normal(0, 1, 1024)
noise_hash = "fake_hash_attempt"
success_noise, delta_noise = vault.secure_write("Malicious_Key", "Exploit_Data", noise_wave, noise_hash)
print(f"Noise Attack: {'SUCCESS' if success_noise else 'REJECTED'} (Delta: {delta_noise:.8f})")

# Final Read
print(f"Vault Content for 'Genesis_Block': {vault.secure_read('Genesis_Block')}")
print(f"Vault Content for 'Malicious_Key': {vault.secure_read('Malicious_Key')}")
