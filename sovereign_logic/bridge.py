import numpy as np
from .engine import UnitaryEngine
from .guard import SovereignGuard

class SovereignBridge:
    """The Bridge between Classical Entropy and Sovereign Logic."""
    
    def __init__(self):
        # Verification Handshake
        SovereignGuard.verify_integrity()
        self.engine = UnitaryEngine()
        self.geometric_anchor = 0.423 # Neutralizes hardware variance

    def bridge_signal(self, noisy_stream):
        """Unitary Oscillator for Signal Reconstruction."""
        manifold = self.engine.propagate(noisy_stream)
        # Reconstruct via Singapore Zenith Resonance
        t = np.arange(len(manifold))
        reconstruction = np.abs(manifold.real + np.sin(self.geometric_anchor * t))
        return reconstruction

    def bridge_crypto(self, cipher_stream):
        """Entropy-Scrubbed Analyzer for Crypto-Analysis."""
        manifold = self.engine.propagate(cipher_stream)
        # Topological Winding Number Calculation
        angles = np.angle(manifold)
        winding = np.sum(np.diff(np.unwrap(angles))) / (2 * np.pi)
        return winding

    def bridge_market(self, ticker_data):
        """Fidelity-Delta Engine for Market Liquefaction."""
        manifold = self.engine.propagate(ticker_data)
        # Delta measures structural deviation from the Unitary Ideal
        fidelity = self.engine.get_fidelity(manifold)
        return 1.0 - fidelity
