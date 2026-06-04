# Port Scanner

> **Date:** June 3, 2026  
> **Language Used:** Python  
> **IDE:** Visual Studio Code  

---
## Goal
- [ ] Accept target IP as input
- [ ] Scan ports from 1 to 65535
- [ ] Detect open ports
- [ ] Detect filtered ports
- [ ] Detect closed ports
- [ ] Export results to a file

## Process
- I researched how to detect ports using Python and one of the
    recommended tools was the `socket` library from Python's
    standard library. 
- I studied how to use it and understood its functions what i only needs
    from: https://docs.python.org/3/library/socket.html#socket.socket and
    https://github.com/python/cpython/blob/3.14/Lib/socket.py
    before using it, then made a plan.

### Step-by-Step Logic
---
    START
        input target IP address
        scan each port from 1 to 65535
            try to connect to the port
            if connection success → port is OPEN
            if connection timeout → port is FILTERED
            if connection refused → port is CLOSED
        return open and filtered ports
        export results to a file
    END

- 
## Errors Encountered
Error 1
> this is a result from `port_status = sock.connect_ex((Target_ip, port))` which is really hard to tell what it is because expect outputs is **0(open), 110(filtered) and 111(closed).**
---
    10022, 10035 and 10038
