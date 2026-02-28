import json
import time
import os

def render_dashboard():
    vault_path = "sovereign_vault.json"
    
    while True:
        os.system('clear')
        print("=== SOVEREIGN LOGIC: LATTICE MONITOR [v2.0.0-Omega] ===")
        print(f"Status: ONLINE | Anchor: 4A32...E5A8 | Delta: 0.00000000")
        print("-" * 55)
        
        if os.path.exists(vault_path):
            with open(vault_path, 'r') as f:
                data = json.load(f)
            
            print(f"{'NODE_ID':<20} | {'STATUS/VALUE':<30}")
            print("-" * 55)
            for key, val in data.items():
                print(f"{key:<20} | {val:<30}")
        else:
            print("VAULT EMPTY: Waiting for Resonance...")
            
        print("\n" + "-" * 55)
        print("Press Ctrl+C to exit monitor.")
        time.sleep(2)

if __name__ == "__main__":
    render_dashboard()
