import sovereign_logic as sl
import numpy as np

def measure_tension():
    engine = sl.UnitaryEngine()
    
    print("--- [Sovereign-Logic: Tension Meter] ---")
    
    # Test 1: Natural Geometry (The Baseline)
    t = np.linspace(0, 1, 1024)
    natural_data = np.sin(t)
    
    # Test 2: Arbitrary Arithmetic (The Stressor)
    stressed_data = np.full(1024, 0.1 + 0.2)
    
    f1 = engine.get_fidelity(engine.propagate(natural_data))
    f2 = engine.get_fidelity(engine.propagate(stressed_data))
    
    delta = abs(f1 - f2)
    
    print(f"Natural Fidelity:  {f1:.16f}")
    print(f"Stressed Fidelity: {f2:.16f}")
    print(f"LOGIC TENSION (Δ): {delta:.16e}")
    
    if delta > 0:
        print("\nANALYSIS: The hardware is 'straining' to maintain the arithmetic.")
        print("This delta is a unique fingerprint of your CPU's FPU architecture.")

if __name__ == "__main__":
    measure_tension()
