# Networking Basics
> **Goal:** Understand how networks work and how devices communicate with each other.  
> **Environment:** VirtualBox / Kali Linux Terminal
---

## Key Concepts
| Concept | Description |
|---------|-------------|
| **Network** | A group of connected devices that can communicate |
| **IP Address** | Unique address assigned to each device on a network |
| **MAC Address** | Hardware address burned into a network interface card |
| **Port** | A number that identifies a specific service on a device |
| **Protocol** | A set of rules for how data is transmitted |
| **DNS** | Translates domain names into IP addresses |
| **Gateway** | The device that connects your network to another network |
| **Subnet** | A smaller network divided from a larger one |
---

## Commands
| Command | Description | Example |
|---------|-------------|---------|
| `ifconfig` | Show network interfaces | `ifconfig` |
| `ip a` | Modern alternative to ifconfig | `ip a` |
| `ping` | Test connectivity to a host | `ping google.com` |
| `traceroute` | Show path packets take to a host | `traceroute google.com` |
| `netstat` | Show network connections | `netstat -an` |
| `ss` | Modern alternative to netstat | `ss -tulnp` |
| `nslookup` | Query DNS records | `nslookup google.com` |
| `dig` | Detailed DNS lookup | `dig google.com` |
| `curl` | Transfer data from a URL | `curl http://example.com` |
| `wget` | Download files from the web | `wget http://example.com/file` |
---

## Network Structure
```
Internet
    └── Router / Gateway
            └── Switch
                    ├── Device A (192.168.1.2)
                    ├── Device B (192.168.1.3)
                    └── Device C (192.168.1.4)
```
---

## OSI Model (Quick Reference)
| Layer | Name | Example |
|-------|------|---------|
| 7 | Application | HTTP, DNS, FTP |
| 6 | Presentation | Encryption, Compression |
| 5 | Session | Login sessions |
| 4 | Transport | TCP, UDP |
| 3 | Network | IP Address |
| 2 | Data Link | MAC Address |
| 1 | Physical | Cables, Wi-Fi signals |
---

## Notes & Observations
- Since i knew the `ip a` i prefer to use it over `ifconfig` — much cleaner, easy to understand and short command.
- I tried to use the `ping` to facebook.com and i think 6.349 avg ping is a good connection. I learned something new how proper way to write command — when i am starting writing commands in zsh, i write like this: `ping facebook.com -D` my flag option is always in the end — i mean both ways works but writing clean and proffessional way is my thing. Claude ai says `ping -D facebook.com` is the correct/standard way. 
- I can't use `traceroute` properly because i'm in VM, my VM hiding the hop on me, i only see the VM route and the rest is `***` it seems blocked or cant view.
- 

---

## Errors Encountered
### Error 1

```
    
```
> Cause:  
> Resolution:  

---

## Practice Checklist
- [ ] View network interfaces using `ifconfig` or `ip a`
- [ ] Test connectivity using `ping`
- [ ] Trace a route using `traceroute`
- [ ] Inspect open ports using `ss -tulnp`
- [ ] Perform a DNS lookup using `nslookup` or `dig`