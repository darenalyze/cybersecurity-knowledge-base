# Process Management
> **Goal:** Understand how Linux manages processes and how to monitor, control, and kill them.  
> **Environment:** VirtualBox / Kali Linux Terminal
---

## Key Concepts
| Concept | Description |
|---------|-------------|
| **Process** | Every running program is a process |
| **PID** | Process ID — unique number assigned to each process |
| **Parent/Child Process** | Every process is spawned from another process |
| **Foreground** | Process running visibly in the terminal |
| **Background** | Process running hidden behind the terminal |
| **Process States** | Running, Sleeping, Stopped, Zombie |
---

## Commands
| Command | Description | Example |
|---------|-------------|---------|
| `ps` | Show running processes | `ps aux` |
| `top` | Live process monitor | `top` |
| `htop` | Improved live process monitor | `htop` |
| `kill` | Kill a process by PID | `kill 1234` |
| `killall` | Kill a process by name | `killall firefox` |
| `bg` | Send process to background | `bg` |
| `fg` | Bring process to foreground | `fg` |
| `jobs` | List background jobs | `jobs` |
| `nice` | Set process priority | `nice -n 10 script.sh` |
| `sleep` | Pause a process | `sleep 5` |
---

## Process Structure
```
systemd (PID 1)        ← root of all processes
    └── bash (PID 200)
            └── firefox (PID 305)  ← child process
```
---
## Process States
| State | Symbol | Meaning |
|-------|--------|---------|
| Running | `R` | Actively using the CPU |
| Sleeping | `S` | Waiting for something |
| Stopped | `T` | Paused by a signal |
| Zombie | `Z` | Finished but not cleaned up |
---
## Notes & Observations
- PID stand for process id. every process in device is have a unique own pid
- It is interesting to know that some process is have "Parent" and "Child" process
- Foreground is a process that the user is actively interacting with. I just know that it is called "Foreground" because I only know before is "Background" which is the process running in background, means you will not get interrupt because this is running in background.
- Proccess is not always means running, there is some types of process and this is where the state process will enter. there is 4 types of process which is, running, stop, zombie and sleeping.
- `ps` allows me to peak at snapshot process center where the current processes live
- if the `ps` only allow me to see the snapshot, the `top` allowing me to see the real-time process.
- You can't use the `htop` right away, when you tried to run the command without installing it first, the terminal will ask you to install it first.
- i really want to try the `bg` and `fg` but idk where to use it, so i try to use `jobs` but nothing showing so, to see if jobs actually working i try to put `sleep 500 &` this means put the terminal into sleep in 500 sec and imediately push it into background. Then i tried to put it in **foreground** using `fg %1` because "1" is the job ID of `sleep 500 $` then my terminal pauses means we puted the job into foreground successfully. I manage to get out of the pause by pressing the **"Ctrl + C"** key also i tried to just quit in current terminal then re-open it and it works too.

---
## ❌ Errors Encountered
 
---
## ✅ Resolution
 
---
## Practice Checklist
- [ ] List all running processes using `ps aux`
- [ ] Monitor live processes using `top` or `htop`
- [ ] Kill a process using `kill` and `killall`
- [ ] Run a process in the background using `bg`
- [ ] Bring a background process to the foreground using `fg`
- [ ] Identify suspicious or unknown processes
