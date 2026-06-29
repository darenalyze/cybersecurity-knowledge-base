# Linux Basic Commands

> **Goal:** Learn and document essential Linux commands for cybersecurity work.  
> **Environment:** VirtualBox / Terminal

---

## Navigation
| Command | Description | Example |
|---------|-------------|---------|
| `pwd`   | Print current directory | `pwd` |
| `ls`    | List files | `ls -la` |
| `cd`    | Change directory | `cd /home/user` |

---

## File Management
| Command | Description | Example |
|---------|-------------|---------|
| `touch` | Create a file | `touch notes.txt` |
| `mkdir` | Create a folder | `mkdir labs` |
| `rm`    | Remove file | `rm notes.txt` |
| `cp`    | Copy file | `cp a.txt b.txt` |
| `mv`    | Move/rename | `mv old.txt new.txt` |

---

## Viewing Files
| Command | Description | Example |
|---------|-------------|---------|
| `cat`   | Print file content | `cat file.txt` |
| `less`  | Scroll through file | `less file.txt` |
| `head`  | First 10 lines | `head file.txt` |
| `tail`  | Last 10 lines | `tail file.txt` |

---

## Permissions
| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change permissions | `chmod 755 script.sh` |
| `chown` | Change ownership | `chown user file.txt` |
| `ls -l` | View permissions | `ls -l` |

---

## Networking Commands
| Command | Description | Example |
|---------|-------------|---------|
| `ping`  | Test connectivity | `ping google.com` |
| `ifconfig` / `ip a` | Show IP info | `ip a` |
| `netstat` | Network stats | `netstat -tulnp` |
| `curl`  | Fetch URL | `curl http://example.com` |

---

## Notes & Observations
- Commands like `ls`, `touch`, and `mkdir` accept multiple arguments,
so you can run them on several targets at once without repeating the command.
(e.g., `touch file1 file2 file3`, `mkdir folder1 folder2 folder3`)
- I want to ping my **IP address** but instead I got an Error [error1](#error-1). I was confused at the commands at first. It looks like `ipconfig` (from Windows command). I looked carefully at the command in linux and it's actually `ifconfig` (I put **"p"** instead of **"f"**)
- I expected using `touch` command on an existing file will create an error but surprisingly it only updates the file's access and modification timestamps.
- I learned that terminal in Linux is case-sensitive unlike Windows terminal.
- The execute (`x`) permission on a plain text file makes no sense since
text files aren't programs. However, `chmod` still matters for text files
and folders — `r` and `w` control who can read or edit them, and `x` on
a folder controls who can enter it.
- I prefer using `ss` over `netstat`. `ss` is much cleaner to read (for me).
- I like how curl works. I can now look at page i want to visit without leaving at my terminal by asking their server to send me a copy of their page.

## Errors Encountered:
### Error 1
---
    Command 'ipconfig' not found, did you mean:
        command 'iwconfig' from deb wireless-tools
        command 'ifconfig' from deb net-tools
        command 'hipconfig' from deb hipcc
      Try: sudo apt install <deb name>
---
**Cause:** I got used to typing `ipconfig` from Windows CMD, but the correct command on Linux is `ifconfig`.  
**Resolution:** Noticing the "f" instead of "p" led me to try ifconfig, which gave the expected result. (Fixed)

## Practice Checklist
- [x] Navigate the file system using only the terminal
- [x] Create, move, and delete files
- [x] Read a file using 3 different commands
- [x] Check your machine's IP address
