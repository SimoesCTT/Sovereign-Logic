import sovereign_logic as sl
import numpy as np

def scan_signal():
    print("--- [Sovereign-Logic: High-Fidelity Signal Scan] ---")
    engine = sl.UnitaryEngine()
    
    # Generate a signal with microscopic "Sovereign" patterns
    # buried under standard IEEE 754 noise.
    t = np.linspace(0, 1, 1024)
    pure_signal = np.sin(2 * np.pi * 5 * t)
    
    # Add noise that standard software would just average out
    noise = np.random.normal(0, 1e-15, 1024) 
    dirty_signal = pure_signal + noise

    print("Analyzing signal for Hidden Structural Integrity...")
    
    # Propagate through the 1024-bit manifold
    manifold = engine.propagate(dirty_signal)
    fidelity = engine.get_fidelity(manifold)
    
    print(f"Detected Signal Fidelity: {fidelity:.16f}")
    
    # The Baseline Comparison
    if fidelity >= 0.9999999999999999:
        print("RESULT: [GRANITE-FIRM] - Hidden Structure Detected.")
        print("This signal is not random noise; it follows a Unitary Law.")
    else:
        print("RESULT: [DECOHERENT] - Pure Entropy.")

if __name__ == "__main__":
    scan_signal()
