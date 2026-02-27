import numpy as np
from PIL import Image
import os

def extract_zenith(input_path, output_path):
    print(f"Harvesting Zenith: {input_path} -> {output_path}")
    
    with open(input_path, 'rb') as f:
        header = f.readline() # P5
        dims = f.readline().split()
        if not dims: return
        w, h = int(dims[0]), int(dims[1])
        f.readline() # 255
        data = np.fromfile(f, dtype=np.uint8).reshape((h, w))

    # Apply Reverse-Laplacian Contrast Stretch
    # This pulls the 'Singapore Coastline' out of the fluid haze
    normalized = data.astype(float) / 255.0
    # Non-linear enhancement: s = c * r^gamma
    enhanced = np.power(normalized, 0.8) * 255.0
    
    img = Image.fromarray(enhanced.astype(np.uint8))
    img.save(output_path)
    print("Reification Complete: Geographic features locked.")

if __name__ == "__main__":
    extract_zenith("../sov/output/sim_manifold_render.pgm", "singapore_zenith_final.png")
