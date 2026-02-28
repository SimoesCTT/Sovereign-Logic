import socket, pickle, struct, sys
from sovereign_logic.lattice import SovereignLattice

def ping_node(ip):
    lattice = SovereignLattice(node_id="CLI-Probe")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)
        client.connect((ip, 5000))
        
        h, w = lattice.issue_challenge()
        data = pickle.dumps({"hash": h, "wave": w})
        client.sendall(struct.pack('>I', len(data)) + data)
        
        resp = pickle.loads(client.recv(4096))
        if resp['success']:
            print(f"SUCCESS: Node [{resp['id']}] LOCKED. Delta: {resp['delta']:.8f}")
        else:
            print("FAILURE: DECOHERENCE DETECTED.")
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    ping_node(sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1")
