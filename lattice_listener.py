import socket, pickle, struct
from sovereign_logic.lattice import SovereignLattice

def receive_all(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet: return None
        data.extend(packet)
    return data

def start_hub():
    lattice = SovereignLattice(node_id="Fedora-Hub")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    print("--- Sovereign Hub Online: Listening for 1024-bit Wave ---")
    try:
        while True:
            conn, addr = server.accept()
            raw_msglen = receive_all(conn, 4)
            if not raw_msglen: continue
            msglen = struct.unpack('>I', raw_msglen)[0]
            data = receive_all(conn, msglen)
            if not data: continue
            
            packet = pickle.loads(data)
            sol = lattice.respond_to_challenge(packet['wave'])
            success, delta = lattice.verify_resonance(packet['hash'], sol)
            
            conn.send(pickle.dumps({"success": success, "delta": delta, "id": "Fedora-Hub"}))
            print(f"[LOCK] Node {addr} Verified. Delta: {delta:.8f}")
            conn.close()
    except KeyboardInterrupt:
        print("\nShutdown.")
    finally:
        server.close()

if __name__ == "__main__":
    start_hub()
