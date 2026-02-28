import socket, json, os
import numpy as np
from sovereign_logic.lattice import SovereignLattice
from sovereign_logic.vault import SovereignVault

def start_hub():
    lattice = SovereignLattice(node_id="Fedora-Hub")
    vault = SovereignVault()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', 5000))
        server.listen(5)
        print("Sovereign Hub v2.0.0-Omega: Online.")
    except Exception as e:
        print(f"Bind Error: {e}")
        return

    while True:
        client, addr = server.accept()
        try:
            # Buffer accumulation for the 1024-bit wave
            data = b""
            client.settimeout(2)
            while True:
                part = client.recv(16384)
                if not part: break
                data += part
                if len(part) < 16384: break
            
            if not data: continue
            
            payload = json.loads(data.decode('utf-8'))
            cmd = payload.get("cmd")
            wave = np.array(payload.get("wave"))
            
            if cmd == "WRITE":
                success, delta = vault.secure_write(
                    payload.get("key"), 
                    payload.get("value"), 
                    wave, 
                    payload.get("hash")
                )
                response = {"status": "LOCKED" if success else "REJECTED", "delta": delta}
            else:
                solution = lattice.respond_to_challenge(wave)
                success, delta = lattice.verify_resonance(payload.get("hash"), solution)
                response = {"node": lattice.node_id, "delta": delta}

            client.send(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print(f"Decoherence Event: {e}")
        finally:
            client.close()

if __name__ == "__main__":
    start_hub()
