import sovereign_logic as sl
import numpy as np

# Initialize the Apex Engine
sl.info()
engine = sl.UnitaryEngine()

# Create chaotic input
chaos = np.random.normal(0, 10, 1024)

# Execute Propagator
manifold = engine.propagate(chaos)
fidelity = engine.get_fidelity(manifold)

print(f"Execution Signature: {engine.signature}")
print(f"Unitary Fidelity:    {fidelity:.16f}")
print("Result: Singapore Zenith Reconstructed.")
