import socket
import os
import threading
from concurrent.futures import ThreadPoolExecutor

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
target_ip = host_ip

open_ports = []
close_ports = []

lock = threading.Lock()

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((target_ip, port))
    sock.close()

    with lock:
        if result == 0:
            open_ports.append(port)
        elif result in (10035, 10061):
            close_ports.append(port)

with ThreadPoolExecutor(max_workers=1000) as executor:
    executor.map(scan_port, range(1, 65536))

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "scan_results.txt")

with open(output_path, "w") as f:
    f.write(f"Open Ports: {sorted(open_ports)}\n")
    f.write(f"Closed Ports: {sorted(close_ports)}\n")