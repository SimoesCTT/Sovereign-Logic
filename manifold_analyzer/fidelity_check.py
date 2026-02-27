# Copyright (c) 2026 Americo Simoes
# Fidelity Comparator: SIM vs Golden Reference

import numpy as np
import sys

def check_fidelity(ref_path, test_path):
    def load_pgm(path):
        with open(path, 'rb') as f:
            f.readline(); f.readline(); f.readline()
            return np.fromfile(f, dtype=np.uint8)

    ref = load_pgm(ref_path)
    test = load_pgm(test_path)
    
    # Calculate Mean Squared Error (MSE) and convert to Fidelity %
    mse = np.mean((ref.astype(float) - test.astype(float))**2)
    fidelity = max(0, 100 - (mse / 65535 * 100))
    
    print("-" * 40)
    print(f"FIDELITY REPORT: {test_path}")
    print(f"System Fidelity: {fidelity:.5f}%")
    print(f"Reihman-Lock Status: {'SECURE' if fidelity > 99.0 else 'BREACHED'}")
    print("-" * 40)

if __name__ == "__main__":
    check_fidelity('data/golden_reference.pgm', sys.argv[1])
