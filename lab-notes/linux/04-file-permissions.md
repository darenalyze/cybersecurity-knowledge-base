# File Permissions
> **Goal:** Understand how Linux controls access to files and directories.
> **Environment:** VirtualBox / Kali Linux Terminal
---

## Permission Basics
| Permission | Symbol | Value |
|------------|--------|-------|
| Read       | `r`    | 4     |
| Write      | `w`    | 2     |
| Execute    | `x`    | 1     |
| No Permission | `-` | 0     |
---

## Commands
| Command | Description | Example |
|---------|-------------|---------|
| `ls -l` | List files with permissions | `ls -l` |
| `chmod` | Change file permissions | `chmod 755 file.sh` |
| `chown` | Change file owner | `chown john file.txt` |
| `chgrp` | Change group owner | `chgrp devs file.txt` |
| `umask` | Default permission mask | `umask 022` |
---

## Numeric (Octal) Mode
| Octal | Permission | Meaning |
|-------|------------|---------|
| `777` | rwxrwxrwx  | Everyone can do everything |
| `755` | rwxr-xr-x  | Owner full, others read/execute |
| `644` | rw-r--r--  | Owner read/write, others read |
| `600` | rw-------  | Owner only |
| `000` | ---------- | No permissions |
---

## Important Files & Permissions
| File | Permission | Why |
|------|------------|-----|
| `/etc/shadow` | `640` | Root read, shadow group only |
| `/etc/passwd` | `644` | Everyone can read |
| `/etc/sudoers` | `440` | Read only, root only |
---

## Notes & Observations
# File Permissions
> **Goal:** Understand how Linux controls access to files and directories.
> **Environment:** VirtualBox / Kali Linux Terminal
---

## Permission Basics
| Permission | Symbol | Value |
|------------|--------|-------|
| Read       | `r`    | 4     |
| Write      | `w`    | 2     |
| Execute    | `x`    | 1     |
| No Permission | `-` | 0     |
---

## Commands
| Command | Description | Example |
|---------|-------------|---------|
| `ls -l` | List files with permissions | `ls -l` |
| `chmod` | Change file permissions | `chmod 755 file.sh` |
| `chown` | Change file owner | `chown john file.txt` |
| `chgrp` | Change group owner | `chgrp devs file.txt` |
| `umask` | Default permission mask | `umask 022` |
---

## Numeric (Octal) Mode
| Octal | Permission | Meaning |
|-------|------------|---------|
| `777` | rwxrwxrwx  | Everyone can do everything |
| `755` | rwxr-xr-x  | Owner full, others read/execute |
| `644` | rw-r--r--  | Owner read/write, others read |
| `600` | rw-------  | Owner only |
| `000` | ---------- | No permissions |
---

## Important Files & Permissions
| File | Permission | Why |
|------|------------|-----|
| `/etc/shadow` | `640` | Root read, shadow group only |
| `/etc/passwd` | `644` | Everyone can read |
| `/etc/sudoers` | `440` | Read only, root only |
---

## Notes & Observations
-  I use `ls -l file1` to check the **file permission** of the **"file1"** it gives me `-rw-rw-r-- 1 dar4sec dar4sec 4 may 20 07:15`. it confused me at first but a bit of research i finnaly break it down. First character `d` means directory, `-` means file which is in our example shown. the set of data `rw-rw-r--` is called "file permissions" or "mode". the `1` called "link". the first `dar4sec` is owner/user. the second `dar4sec` one is called "group", and the last data is a date when the file last modified.
- `chmod 777` is dangerous. gives everyone full access.
- i put `000` value on file1 for just example using chmod and i tried to copy a file and paste it, expecting that new pasted file have default permission. but that is not what happened. when i am about to paste the file1 the error showed up "Error opening file Permission denied"
- I used user `dar4sec` to create a file and created a file called file2. I switch to the user `attacker` and tried to change the ownership of the file2 using `chown`, my first attemp it did not worked because of the error `Opperation not permitted` so i used `sudo` and in my surprised it Worked!
- I created a my own group to test the `chgrp` at the safer environment and i call this group `mygroup`. As a default the group owner is the one created the file/directory but we can change the group owner by just using `chgrp` and also only one group owner can put in file or directory.
- `unmask` is interesting one for me, it let u minus the value of the inputed val in mask to default val of the permision of the file/directory (the default val of the file is 644) that is why they often use `unmask 022`= 644 - 022 so the "other" and "group" have permission to read only.
---

## ❌ Errors Encountered
Error 1
---
    Error opening file Permission denied
---
Error 2
---
    Opperation not permitted
---
## ✅ Resolution
### "Error 1, 2" 
1. **Permission denied** — The file had `000` permissions. Used `sudo chmod` to restore permissions. (✅ fixed)
2. **Operation not permitted** — Regular users cannot change file ownership. Used `sudo` before `chown` to run it as root. (✅ fixed)
---
## Practice Checklist
- [x] Check permissions of a file using `ls -l`
- [x] Change permissions using `chmod`
- [x] Change ownership using `chown`
- [ ] Check permissions of `/etc/shadow` and `/etc/passwd`
- [ ] Create a script and make it executable
---

## ❌ Errors Encountered
Error 1
---
    Error opening file Permission denied
---
Error 2
---
    Opperation not permitted
---
## ✅ Resolution
### "Error 1, 2" 
- I used sudo to use the root permission
---
## Practice Checklist
- [x] Check permissions of a file using `ls -l`
- [x] Change permissions using `chmod`
- [x] Change ownership using `chown`
- [ ] Check permissions of `/etc/shadow` and `/etc/passwd`
- [ ] Create a script and make it executable
