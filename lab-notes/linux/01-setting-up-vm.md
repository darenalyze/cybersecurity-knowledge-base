# Setting up the Linux VM

## Specifications
* **Hypervisor:** Oracle VirtualBox
* **OS ISO used:** Kali Linux
* **RAM allocated:** 2GB
* **Storage allocated:** 20GB

## Objective:
- Set up a Kali Linux VM on VirtualBox as a safe, isolated environment
for cybersecurity practice and future labs.

## Steps Taken:
1. Download the VM https://www.virtualbox.org/wiki/Downloads and install.
2. Created a new VM in VirtualBox:
   - Type: Linux / Debian (64-bit)
   - RAM: 2048 MB
   - Created a virtual hard disk (VDI, 20GB, dynamically allocated)
3. Attached the Kali Linux ISO to the VM's optical drive
4. Started the VM and followed the Kali installer

## ❌ Errors Encountered:
- `VERR_SVM_DISABLED`

## ✅ Resolution:
1. Booted into BIOS and enabled **Virtualization (SVM Mode)** (✅Fixed)
   
## Lessons Learned:
- VirtualBox requires **hardware virtualization** to be on at the firmware level
