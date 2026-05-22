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
- **Error 1** (Initial Setup)
---
    VERR_SVM_DISABLED
---
- (4:49 am 5/21/2026)
---
    Could not start the machine kali linux because the following physical network interfaces were not found:
    Realtek PCIe GbE Family Controller (adapter 1)
    You can either change the machine's network settings or stop the machine.
---

## ✅ Resolution:
1. 
   - Booted into the motherboard BIOS and enabled **Virtualization (SVM Mode)**. (Fixed initial setup error)
2. 
   - Open VirtualBox VM **Settings -> Network -> Adapter 1**.
   - Under **Name**, changed the dropdown selection from the old network controller to the new hardware interface (`Realtek PCIe GbE Family Controller #2`).
   - Clicked **OK** to save and successfully booted the VM. (Fixed 4: 55 am 5/21/2026)

## Lessons Learned:
- VirtualBox requires **hardware virtualization** to be on at the firmware level
- Changing or upgrading physical hardware (like a CPU or motherboard) can alter hardware identifiers, requiring VM network settings to be remapped.