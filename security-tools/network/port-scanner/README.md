# Port Scanner
> **Date:** June 3, 2026
> **Language Used:** Python
> **IDE:** Visual Studio Code
---
 
## Goal
- [x] Accept target IP as input
- [x] Scan ports from 1 to 1024
- [x] Scan ports full range (1 to 65,535)
- [x] Detect open ports
- [x] Detect closed ports
- [x] Export results to a file

---
## New Features
- 6/6/2026 
  - 10061 (WSAECONNREFUSED) added as a second closed condition. Unlike 10035 which is a timeout/no-response, this code means the target actively rejected the connection, which is closed state.
- 6/6/2026 
  - The result of **Closed, Open and Other Ports** will be transferred in file instead of just printing the output in terminal.
- 6/6/2026 
  - Restructured into its own folder. Renamed `port-scanner.py` to `main.py`.
- 6/7/2026 
  - Moved port-scanner from automation-scripts to security-tools/network/
- 6/11/2026
  - Improved performance using threading
    - Replaced sequential loop with `ThreadPoolExecutor(max_workers=1000)` from `concurrent.futures`
    - Added `threading.Lock()` to prevent race conditions when multiple threads append to the same list simultaneously
    - Added `import threading` required separately even when using `ThreadPoolExecutor`
    - Expanded scan range from 1–1024 to 1–65535
    - Removed `other_ports` list — reduces unnecessary locking across 65535 ports
  - Benchmark result: 1–65535 scanned in ~6 seconds (~1000x faster than original sequential scan)

## Process
- Researched how to detect port states using Python. The recommended tool was the `socket` library from Python's standard library.
- Studied the official documentation and source before writing any code:
  - https://docs.python.org/3/library/socket.html#socket.socket
  - https://github.com/python/cpython/blob/3.14/Lib/socket.py
- Discovered that `connect_ex()` returns integer error codes from the OS (not exceptions), making it cleaner to use inside a loop compared to `connect()`.
- Windows uses **WSA (Windows Sockets API)** error codes, which are different from Linux error codes. An `other-port` list was added to catch any unrecognized codes rather than silently dropping them.
- I put the `sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` inside the loop because it gives me `10038` as a socket state issue caused by reusing a closed socket.
- The use of `connect_ex()` instead of using `connect()` is because `connect_ex()` returns integer error codes instead of raising exceptions, making it cleaner to handle inside a loop without try/except.
- Setting the timeout to `(1)` is kinda slow for me so I decided to switch to 0.1. I think that is still good because port is fast at responding when Open.
- I use terminal for an output in the meantime because it is more convenient and easy to debug something.
- Replaced sequential loop with `ThreadPoolExecutor` to scan ports concurrently. Used `threading.Lock()` to prevent race conditions when multiple threads write to the same list. Removed `other_ports` list to reduce unnecessary locking across 65535 ports.

### Step-by-Step Logic
```
START
    resolve hostname to target IP
    spawn 1000 threads via ThreadPoolExecutor
    each thread scans one port:
        create a new TCP socket
        set timeout to 0.05 seconds
        attempt connection via connect_ex()
        acquire lock
            if result == 0             → port is OPEN
            if result in (10035,10061) → port is CLOSED
        release lock
        close socket
    write sorted open and closed port lists to file
END
```
---
 
## WSA Error Code Reference
| Code | Name | Meaning |
|------|------|---------|
| `0` | Success | Port is **open** |
| `10013` | `WSAEACCES` | Permission denied — run as Administrator |
| `10022` | `WSAEINVAL` | Invalid argument — bad socket setup |
| `10035` | `WSAEWOULDBLOCK` | Still trying / no answer within timeout — treated as **closed** |
| `10038` | `WSAENOTSOCK` | Not a socket — socket was already closed |
| `10048` | `WSAEADDRINUSE` | Address already in use |
| `10049` | `WSAEADDRNOTAVAIL` | Address not available — IP does not exist |
| `10051` | `WSAENETUNREACH` | Network unreachable — no route to target |
| `10054` | `WSAECONNRESET` | Connection reset by target |
| `10060` | `WSAETIMEDOUT` | Timed out — actual timeout code |
| `10061` | `WSAECONNREFUSED` | Connection refused — port is **closed** (clean rejection) |
| `10064` | `WSAEHOSTDOWN` | Host is down |
| `10065` | `WSAEHOSTUNREACH` | Host unreachable |
> **Note:** `10035` does not mean "timed out" — it means "would block," which is Windows telling the socket it hasn't resolved yet. Since the scanner moves on after the timeout, it is treated as closed in practice. The actual timeout code is `10060`.
---
 
## Errors Encountered

### Error 1 — Unexpected result codes from `connect_ex()`
> **Expected outputs:** `0` (open), `110` (filtered), `111` (closed)  
**Actual outputs:** `10035`, `10038`  
**Cause:** The expected codes `110` and `111` are Linux-only. Windows uses WSA error codes instead.  
**Resolution:** Researched Windows-specific codes. Mapped `10035` as closed (still trying / no answer) and `10038` as a socket state issue caused by reusing a closed socket. Fixed by creating a new socket for each port inside the loop.
---
 
### Error 2 — Port `137` appearing in `other` list
> **Cause:** Port `137` is a **UDP port** (NetBIOS Name Service). The scanner uses `SOCK_STREAM` which is TCP only. TCP cannot properly connect to a UDP port, so it returns an unrecognized code instead of `0` or `10035`.  
**Resolution:** Logged it in the `other` list. A full scanner would require a separate `SOCK_DGRAM` socket to scan UDP ports.
 


