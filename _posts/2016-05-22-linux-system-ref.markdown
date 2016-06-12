---
layout: post
title:  "Linux System Reference"
date:   2016-05-22 13:14:00 -0500
categories: linux
description: "linux system links and sources"
---


### Creating a new user
```bash
sudo useradd jonsmith
sudo passwd jonsmith
sudo mkhomedir_helper jonsmith
```


### The Issue
I installed kali linux and everything worked. amazing. never happeded to me before.
how did this happen?

what is the difference between firmware and device drivers?

Firmware is simply software that is stored in non-volatile semiconductor memory 
(e.g. PROM, EEPROM or flash) chips rather than a mass storage device such as a hard drive

driver: software that lets your os talk to the hardware
firmware: which is usually a small piece of code that is 
uploaded directly to the device for it to function correctly

```bash
ls /
```

file: 0
directory: bin
directory: boot
directory: dev
directory: etc
directory: home
file: initrd.img
directory: lib
directory: lib64
directory: lost+found
directory: media
directory: mnt
directory: opt
directory: proc
directory: root
directory: run
directory: sbin
directory: srv
directory: sys
directory: tmp
directory: usr
directory: var
file: vmlinuz




/bin

This directory contains basic commands and programs that are needed to achieve a minimal working environment upon booting. These are kept separate from some of the other programs on the system to allow you to boot the system for maintenance even if other parts of the filesystem may be damaged or unavailable.

If you search this directory, you will find that both ls and pwd reside here. The cd command is actually built into the shell we are using (bash), which is in this directory too.

/boot

This directory contains the actual files, images, and kernels necessary to boot the system. While /bin contains basic, essential utilities, /boot contains the core components that actually allow the system to boot.

If you need to modify the bootloader on your system, or if you would like to see the actual kernel files and initial ramdisk (initrd), you can find them here. This directory must be accessible to the system very early on.

/dev

This directory houses the files that represent devices on your system. Every hard drive, terminal device, input or output device available to the system is represented by a file here. Depending on the device, you can operate on the devices in different ways.

For instance, for a device that represents a hard drive, like /dev/sda, you can mount it to the filesystem to access it. On the other hand, if you have a file that represents a line printer like /dev/lpr, you can write directly to it to send the information to the printer.

/etc

This is one area of the filesystem where you will spend a lot of time if you are working as a system administrator. This directory is basically a configuration directory for various system-wide services.

By default, this directory contains many files and subdirectories. It contains the configuration files for most of the activities on the system, regardless of their function. In cases where multiple configuration files are needed, many times a application-specific subdirectory is created to hold these files. If you are attempting to configure a service or program for the entire system, this is a great place to look.

/home

This location contains the home directories of all of the users on the system (except for the administrative user, root). If you have created other users, a directory matching their username will typically be created under this directory.

Inside each home directory, the associated user has write access. Typically, regular users only have write access to their own home directory. This helps keep the filesystem clean and ensures that not just anyone can change important configuration files.

Within the home directory, that are often hidden files and directories (represented by a starting dot) that allow for user-specific configuration of tools. You can often set system defaults in the /etc directory, and then each user can override them as necessary in their own home directory.

/lib

This directory is used for all of the shared system libraries that are required by the /bin and /sbin directories. These files basically provide functionality to the other programs on the system. This is one of the directories that you will not have to access often.

/lost+found

This is a special directory that contains files recovered by /fsck, the Linux filesystem repair program. If the filesystem is damaged and recovery is undertaken, sometimes files are found but the reference to their location is lost. In this case, the system will place them in this directory.

In most cases, this directory will remain empty. If you experience corruption or any similar problems and are forced to perform recovery operations, it's always a good idea to check this location when you are finished.

/media

This directory is typically empty at boot. Its real purpose is simply to provide a location to mount removable media (like cds). In a server environment, this won't be used in most circumstances. But if your Linux operating system ever mounts a media disk and you are unsure of where it placed it, this is a safe bet.

/mnt

This directory is similar to the /media directory in that it exists only to serve as a organization mount point for devices. In this case, this location is usually used to mount filesystems like external hard drives, etc.

This directory is often used in a VPS environment for mounting network accessible drives. If you have a filesystem on a remote system that you would like to mount on your server, this is a good place to do that.

/opt

This directory's usage is rather ambiguous. It is used by some distributions, but ignored by others. Typically, it is used to store optional packages. In the Linux distribution world, this usually means packages and applications that were not installed from the repositories.

For instance, if your distribution typically provides the packages through a package manager, but you installed program X from source, then this directory would be a good location for that software. Another popular option for software of this nature is in the /usr/local directory.

/proc

The /proc directory is actually more than just a regular directory. It is actually a pseudo-filesystem of its own that is mounted to that directory. The proc filesystem does not contain real files, but is instead dynamically generated to reflect the internal state of the Linux kernel.

This means that we can check and modify different information from the kernel itself in real time. For instance, you can get detailed information about the memory usage by typing cat /proc/meminfo.

/root

This is the home directory of the administrative user (called "root"). It functions exactly like the normal home directories, but is housed here instead.

/run

This directory is for the operating system to write temporary runtime information during the early stages of the boot process. In general, you should not have to worry about much of the information in this directory.

/sbin

This directory is much like the /bin directory in that it contains programs deemed essential for using the operating system. The distinction is usually that /sbin contains commands that are available to the system administrator, while the other directory contains programs for all of the users of the system.

/selinux

This directory contains information involving security enhanced Linux. This is a kernel module that is used to provide access control to the operating system. For the most part, you can ignore this.

/srv

This directory is used to contain data files for services provided by the computer. In most cases, this directory is not used too much because its functionality can be implemented elsewhere in the filesystem.

/tmp

This is a directory that is used to store temporary files on the system. It is writable by anyone on the computer and does not persist upon reboot. This means that any files that you need just for a little bit can be put here. They will be automatically deleted once the system shuts down.

/usr

This directory is one of the largest directories on the system. It basically includes a set of folders that look similar to those in the root / directory, such as /usr/bin and /usr/lib. This location is basically used to store all non-essential programs, their documentation, libraries, and other data that is not required for the most minimal usage of the system.

This is where most of the files on the system will be stored. Some important subdirectories are /usr/local, which is an alternative to the /opt directory for storing locally compiled programs. Another interesting thing to check out is the /usr/share directory, which contains documentation, configuration files, and other useful files.

/var

This directory is supposed to contain variable data. In practice, this means it is used to contain information or directories that you expect to grow as the system is used.

For example, system logs and backups are housed here. Another popular use of this directory is to store web content if you are operating a web server.



[1](http://superuser.com/questions/299442/difference-and-relation-between-firmware-and-device-driver)
[2](https://wiki.ubuntu.com/Kernel/Firmware)
