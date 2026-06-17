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
- Error 1 VERR_SVM_DISABLED (Initial Setup)
> **Cause**: VM needs a **Virtualization (SVM Mode)**  
> **Resolution**: Booted into the motherboard BIOS and enabled **Virtualization (SVM Mode)**. (Fixed initial setup error)

- Error 2 Realtek PCIe GbE Family Controller (adapter 1) (4:49 am 5/21/2026)
> **Cause:** Changing CPU Hardware  
> **Resolution:**  
> - Open VirtualBox VM **Settings** -> **Network** -> **Adapter 1**.
> - Under **Name**, changed the dropdown selection from the old network controller to the new hardware interface (`Realtek PCIe GbE Family Controller #2`).
> - Clicked **OK** to save and successfully booted the VM. (Fixed 4: 55 am 5/21/2026)

- Error 3 Black screen after boot (6/10/2026)
> **Cause:** Corrupted file in graphical interface side I think. because there is poping text of error graphics even tho i already restarted the pc and the GPU is perfectly working. Because what I remember I shutdown the pc while there is a active proccess and while the VM shutting down (that was the possible culprit i can think off)  
**Resolution:**  
   - Waited about 5mins (failed)
   - Switching to Terminal:
     - pressing `Ctrl + Alt + F2` while in boot loader
     - I log-in (seems all alright here and all folder and files are saved, idk why in GUI is have a problem)
     - I type `sudo systemctl restart gdm3` (error) so i tried:
     - `sudo service display-manager restart` but still black screen after
     - In GRUB menu i choose "Kali GNU/Linux and pressed E
     - Appended `nomodeset` to the GRUB boot parameters (failed).
   - Last Resort: 
      - Re-install the os (fixed 6/10/2026)

## Lessons Learned:
- VirtualBox requires **hardware virtualization** to be on at the firmware level
- Changing or upgrading physical hardware (like a CPU or motherboard) can alter hardware identifiers, requiring VM network settings to be remapped.
