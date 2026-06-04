import socket

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
    elif result == 10035:
        close_ports.append(port)
        #print(f"{port}: Close")
    else:
        other_ports.append(port)
        #print(f"{port}: {result}")
    sock.close()
print(f"Open Ports: {open_ports}")
print(f"Close Ports: {close_ports}")
print(f"Other Ports: {other_ports}")
