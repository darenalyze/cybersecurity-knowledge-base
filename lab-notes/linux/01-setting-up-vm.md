# Lab Setup: Setting up the Linux VM

## Specifications
* **Hypervisor:** Oracle VirtualBox
* **OS ISO used:** Kali Linux
* **RAM allocated:** 2GB
* **Storage allocated:** 20GB

## Objective:
- Run the VM Smoothly

## Steps Taken:
1. Download the VM https://www.virtualbox.org/wiki/Downloads and install.
2. Setup my virtual machine
3. Tried to start but got the <font color="red">**ERROR**</font>

## Errors:
- `VERR_SVM_DISABLED`

## Resolution:
1. Booted into the motherboard BIOS and enabled **Virtualization** (SVM Mode) <font color="green">**(Fixed)**</font>