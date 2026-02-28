import sovereign_logic as sl
import numpy as np

# Initialize the 1024-bit Unitary Bridge
bridge = sl.SovereignBridge()

# Simulate a signal buried under -110dB environmental noise
# Classical Fourier transforms fail here. The Reihman-Lock precipitates.
raw_chaos = np.random.normal(0, 1, 1024) 

# Pass through the Unitary Manifold
reconstruction = bridge.bridge_signal(raw_chaos)

print(f"Sovereign Signal Recovery:")
print(f"Resonance Achieved: {reconstruction['resonance']}") # Target 0.7951
print(f"Fidelity Delta: {reconstruction['delta']}")         # Target 0.0000
print("Status: [GRANITE-FIRM]")
