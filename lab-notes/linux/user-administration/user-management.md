# Linux User Management
> **Goal:** Understand how Linux manages users, groups, and privileges.  
> **Environment:** VirtualBox / Kali Linux Terminal
---
## Users
| Command | Description | Example |
|---------|-------------|---------|
| `whoami` | Show current user | `whoami` |
| `id` | Show user ID and groups | `id` |
| `who` | Show logged-in users | `who` |
| `adduser` | Create a new user | `sudo adduser john` |
| `passwd` | Change password | `passwd john` |
| `deluser` | Delete a user | `sudo deluser john` |
---
## Groups
| Command | Description | Example |
|---------|-------------|---------|
| `groups` | Show groups of current user | `groups` |
| `addgroup` | Create a new group | `sudo addgroup devs` |
| `usermod` | Add user to a group | `sudo usermod -aG devs john` |
| `delgroup` | Delete a group | `sudo delgroup devs` |
---
## Switching Users & Privileges
| Command | Description | Example |
|---------|-------------|---------|
| `su` | Switch to another user | `su john` |
| `su -` | Switch to root | `su -` |
| `sudo` | Run command as root | `sudo apt update` |
| `sudo -l` | List your sudo permissions | `sudo -l` |
---
## Important Files
| File | Description |
|------|-------------|
| `/etc/passwd` | Stores user account info |
| `/etc/shadow` | Stores hashed passwords |
| `/etc/group` | Stores group info |
---
## Notes & Observations
- I often use `whoami` because I always check if I am on the right user. This will be useful when you have 2 or more users on one computer (I am planning to create 2 users — one for attack, one for defense).
- For me `who` is perfect for checking currently logged-in users.
- [error2](#error-2) — having this error means I can't add a user or create a user by default for a newly created user, even with sudo, because the attacker is not in the sudoers group.
- Running `sudo -l` I realize that there is a limit in sudo and it depends on your permission.
- I often use `cat /etc/passwd` to check the users I created and delete some that I am not using anymore using `sudo deluser [username]`.
- `su` it lets you switch users easily without needing to restart your PC completely.
- Running `cat /etc/shadow` gave me unexpected output [error4](#error-4) I think because `/etc/shadow` is restricted to root only by its file permissions, so regular users cannot read it.
- I learned that all files and folders in the root directory require `sudo` to bypass 
basic permissions and perform actions there.
---
## Errors Encountered
### Error 1
```
    Fatal: Only root may add a user or group to the system.
```
> Cause: Only root may add a user or group to the system.
> Resolution: Used `sudo` before the command to run it as root. (fixed)

### Error 2
```
    attacker is not in the sudoers file.
       |
    (username)
```
> Cause: Attacker user is not in the sudoers group
> Resolution: Added the user to the `sudo` group using `sudo usermod -aG sudo (username)` to grant sudo privileges. (fixed)

### Error 3
```
    su: Authentication failure
```
> Cause: Just a wrong input password.
> Resolution: Used `sudo` before the command to run it as root. (fixed)
### Error 4
```
    cat: /etc/shadow: Permission denied
```

> Cause: The file or folder is restricted and requires higher-level permissions.
> Resolution: Run `sudo` before the command.

## Resolution

## Practice Checklist
- [x] Check your current user and ID
- [x] Create a new user and set a password
- [x] Create a group and add the new user to it
- [x] Switch to the new user using `su`
- [x] Run a command with `sudo` and check your sudo permissions
- [x] Read `/etc/passwd` and identify your user entry
