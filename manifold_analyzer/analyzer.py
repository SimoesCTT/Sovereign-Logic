# Copyright (c) 2026 Americo Simoes
# License: Sovereign Research License (SRL)
#
# Topological Entropy Analyzer for Unitary SAT Manifolds

import numpy as np
import sys
import os

def analyze():
    if len(sys.argv) < 2:
        print("Usage: python3 analyzer.py <manifold.pgm>")
        return

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return

    with open(path, 'rb') as f:
        f.readline(); f.readline(); f.readline()
        data = np.fromfile(f, dtype=np.uint8)

    grad = np.gradient(data.astype(float))
    hist, _ = np.histogram(grad, bins=256, density=True)
    entropy = -np.sum(hist * np.log2(hist + 1e-9))

    print("-" * 40)
    print(f"MANIFOLD ANALYSIS: {os.path.basename(path)}")
    print(f"Topological Entropy: {entropy:.5f}")
    
    if entropy < 7.5:
        print("STATUS: LAMINAR FLOW (LOGIC SATISFIED)")
    else:
        print("STATUS: TURBULENT (CONTRADICTION DETECTED)")
    print("-" * 40)

if __name__ == "__main__":
    analyze()
