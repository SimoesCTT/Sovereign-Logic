import sovereign_logic as sl
import numpy as np

def run_fortress_test():
    print("--- [Sovereign-Logic: Deterministic Fortress Test] ---")
    
    # 1. Standard Computing 'Noise'
    a = 0.1
    b = 0.2
    standard_sum = a + b
    print(f"Standard IEEE 754 Sum: {standard_sum:.20f}")
    
    # 2. Initialize the Unitary Engine (The Sentinel)
    engine = sl.UnitaryEngine()
    
    # 3. Inject the 'Noisy' Sum into the 1024-bit Manifold
    # We treat the error as 'Entropy' for the Propagator
    test_data = np.full(1024, standard_sum)
    
    # The Reihman-Lock Hamiltonian compresses the 0.000...04 noise
    manifold = engine.propagate(test_data)
    fidelity = engine.get_fidelity(manifold)
    
    print(f"Manifold Fidelity:     {fidelity:.16f}")
    
    if fidelity == 1.0:
        print("RESULT: [GRANITE-FIRM] - Noise Neutralized.")
        print("The Fortress holds. The Singapore Zenith is Absolute.")
    else:
        print("RESULT: DECOHERENCE - Hardware Variance Detected.")

if __name__ == "__main__":
    run_fortress_test()
