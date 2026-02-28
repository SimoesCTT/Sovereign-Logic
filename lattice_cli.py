import socket, json, sys
import numpy as np
from sovereign_logic.lattice import SovereignLattice

def run_cli(ip, cmd="PING", key=None, value=None):
    lattice = SovereignLattice(node_id="Remote-Lattice-Client")
    wave = lattice.generate_unitary_wave()
    wave_hash = lattice.respond_to_challenge(wave)
    
    # Convert wave to list for JSON compatibility
    payload = {
        "cmd": cmd,
        "wave": wave.tolist(),
        "hash": wave_hash,
        "key": key,
        "value": value
    }
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, 5000))
            s.sendall(json.dumps(payload).encode('utf-8'))
            
            resp = s.recv(4096).decode('utf-8')
            response = json.loads(resp)
            
            if cmd == "WRITE":
                print(f"VAULT: {response.get('status')} | Delta: {response.get('delta'):.8f}")
            else:
                print(f"NODE: {response.get('node')} | Delta: {response.get('delta'):.8f}")
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    if len(sys.argv) >= 5 and sys.argv[2] == "WRITE":
        run_cli(target, "WRITE", sys.argv[3], sys.argv[4])
    else:
        run_cli(target)
