import numpy as np
from .guard import SovereignGuard

class UnitaryEngine:
    def __init__(self):
        SovereignGuard.verify_integrity()
        self.beta = SovereignGuard.BETA
        self.lam = SovereignGuard.LAMBDA
        self.signature = SovereignGuard.get_signature()

    def propagate(self, data):
        data_norm = (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-9)
        energy = np.tanh(self.beta * (data_norm - 0.5) * self.lam)
        theta = energy * (33.0 / self.beta)
        return np.cos(theta) + 1j * np.sin(theta)

    def get_fidelity(self, manifold):
        return np.mean(np.abs(manifold)**2)
