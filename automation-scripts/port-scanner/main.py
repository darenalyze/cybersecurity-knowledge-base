import socket
import os

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
target_ip = host_ip

open_ports = []
close_ports = []
other_ports = []


for port in range(1, 1025):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((target_ip, port))
    
    if result == 0:
        open_ports.append(port)
        #print(f"{port}: Open")
    elif result in (10035, 10061):
        close_ports.append(port)
        #print(f"{port}: Close")
    else:
        other_ports.append(port)
        #print(f"{port}: {result}")
    sock.close()
    
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "scan_results.txt")

with open(output_path, "w") as f:
    f.write(f"Open Ports: {open_ports}\n")
    f.write(f"Closed Ports: {close_ports}\n")
    f.write(f"Other Ports: {other_ports}\n")
