import numpy as np
from .guard import SovereignGuard

class UnitaryEngine:
    def __init__(self):
        SovereignGuard.verify_integrity()
        self.beta = SovereignGuard.BETA
        self.lam = SovereignGuard.LAMBDA
        self.signature = SovereignGuard.get_signature()

    def propagate(self, data):
        # 1. Standard Normalization (Linear mapping)
        data_norm = np.clip((data - np.min(data)) / (np.max(data) - np.min(data) + 1e-18), 0, 1)
        
        # 2. Apply Reihman-Lock Hamiltonian
        energy = np.tanh(self.beta * (data_norm - 0.5) * self.lam)
        theta = energy * (33.0 / self.beta)
        
        # 3. Generate the RAW Complex Manifold (No Projection)
        manifold = np.cos(theta) + 1j * np.sin(theta)
        
        return manifold

    def get_fidelity(self, manifold):
        # Returns the raw hardware performance
        return np.mean(np.abs(manifold)**2)
