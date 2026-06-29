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
- PID stands for Process ID. Every process on a device has its own unique PID.
- It is interesting to know that some processes have a "Parent" and "Child" relationship.
- Foreground is a process that the user is actively interacting with. I just learned it's called "Foreground" — before this, I only knew "Background," which is a process running behind the scenes, meaning it won't interrupt you.
- A process is not always running. There are types of states a process can be in — 4 to be exact: Running, Stopped, Zombie, and Sleeping.
- `ps` allows me to peek at a snapshot of where the current processes live.
- If `ps` only lets me see a snapshot, `top` lets me see processes in real-time.
- You can't use `htop` right away — when you try to run the command without installing it first, the terminal will prompt you to install it.
- I really wanted to try `bg` and `fg` but didn't know where to start, so I tried `jobs` first — but nothing showed up. To verify it actually works, I ran `sleep 500 &`, which puts the terminal to sleep for 500 seconds and immediately pushes it to the background. Then I brought it to the foreground using `fg %1`, since "1" is the job ID of `sleep 500 &`. My terminal paused, which confirmed the job moved to the foreground successfully. I got out of the pause by pressing **Ctrl + C.** I also tried just closing the terminal and reopening it — that worked too.
- When I used `nice` on a running program, it threw [Error 1](#error-1). I realized you can only use `nice` on a process that doesn't exist yet. The command I was looking for is `renice`, which lets you modify the niceness of an already-running process. `renice` expects a PID, so when I passed the process name instead, it threw [Error 2](#error-2).
- I prefer `killall` over `kill` — `kill` requires the PID and only targets that specific 
process, which can leave child processes running or even cause them to respawn.
---
## Errors Encountered
### Error 1

```
    nice: cannot set niceness: Permission denied
    nice: ‘18700’: No such file or directory
```
> Cause: The program expects a name, not a PID, and requires root/administrative access.  
> Resolution: Used the real name of the program and used `sudo` (fixed).

### Error 2
 
```
    renice: bad process ID value: brave
```
> Cause: renice expects a PID — I assumed it took the same input as nice.  
> Resolution: I run `top` to see existing process PID runnign and used that instead of name of the process(fixed).
---

## Practice Checklist
- [x] List all running processes using `ps aux`
- [x] Monitor live processes using `top` or `htop`
- [x] Kill a process using `kill` and `killall`
- [x] Run a process in the background using `bg`
- [x] Bring a background process to the foreground using `fg`
