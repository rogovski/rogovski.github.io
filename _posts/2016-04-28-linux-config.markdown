---
layout: post
title:  "Linux Configuration"
date:   2016-04-28 13:14:00 -0500
categories: linux
description: "links and sources"
---


[SO answer](http://stackoverflow.com/a/1024121)

1. Generally system/global config is stored somewhere under /etc.
2. User-specific config is stored in the user's home directory, often as a hidden file, sometimes as a hidden directory containing non-hidden files (and possibly more subdirectories).

Generally speaking, command line options will override environment variables which will override user defaults which will override system defaults.

$ scp ~/script machine:/home/user

### list block devices

```bash
lsblk
```

http://www.cyberciti.biz/faq/howto-format-create-linux-filesystem/

mkfs -t filetype /dev/DEVICE
OR
mkfs.ext3 /dev/DEVICE
OR
mkfs.ext4 /dev/DEVICE

mkdir /SomeCustomMountPoint

mount /dev/sdb /SomeCustomMountPoint

http://www.linfo.org/umount.html

https://en.wikipedia.org/wiki/Ext4
-- see part about windows and mac compat



How to Prepare the USB Flash Drive on a Linux (Red Hat/SUSE) System

Before You Begin

This procedure requires the use of parted utility version 1.8.6 or later. Do not use earlier versions of parted.

Extract (unzip) the contents of the syslinux-version.zip archive file.

# unzip syslinux-version.zip

Where version represents the Syslinux version number.

Insert the USB flash drive into a working USB 2.0 port.

Use the tail command to identify the USB flash drive’s device name.

# tail /var/log/messages

You should see the device name (such as, sda or sdb). Example output is shown below:

Nov 12 13:19:29 server kernel: scsi 4:0:0:0: Lexar, Inc. USBdisk PQ: 0 ANSI: 0 CCS
Nov 12 13:19:29 server kernel: sd 4:0:0:0: [sdb] 1030750208 512-byte hardware sectors (1030 MB)
Nov 12 13:19:29 server kernel: sd 4:0:0:0: [sdb] Write Protect is off
Nov 12 13:19:29 server kernel: sd 4:0:0:0: [sdb] Assuming drive cache: write through
Nov 12 13:19:29 server kernel: sdb:
Nov 12 13:19:29 server kernel: sd 4:0:0:0: [sdb] Attached SCSI removable disk
Nov 12 13:19:29 server kernel: sd 4:0:0:0: Attached scsi generic sg2 type 0
Caution 
Caution - Be sure to confirm and make a note of the device name of the USB flash drive (/dev/sda, /dev/sdb, etc.). The instructions listed here require you to delete existing partition(s) on the USB flash disk. Making a mistake in identifying the device might cause you to erase a hard disk.

Create a single bootable partition on the USB flash drive using parted, as follows:

Note - This procedure requires the use of parted utility version 1.8.6 or later. Do not use earlier versions of parted.

Note - These steps require superuser (su - root) access.

If Linux has automounted the device, unmount it first.

# umount /dev/sdX1

Where X is the drive letter for the USB flash drive (for example, /dev/sda or /dev/sdb), and 1 indicates the first partition.

Use parted to delete all partitions and create a new bootable FAT32 partition:

# /sbin/parted /dev/sdX

Where X is the drive letter for the USB flash drive (for example, /dev/sda or /dev/sdb).

The parted command prompt displays.

Enter the following commands in the order listed and follow the prompts to create your bootable primary partition:

(parted): mklabel

You will be prompted to create a disk label type. If msdos is not listed as the default, you will need to enter msdos at the appropriate prompt, as shown in the example below:

Warning: The existing label on sdx will be destroyed and all 
data on this disk will be lost. Do you want to continue?
Yes/No: yes
New disk label type? msdos
(parted): mkpartfs

Creates a new partition on the disk. Answer the prompts to confirm that this will be the primary partition, fat32 format, spanning the entire disk minus the last megabyte (starting at 1, and ending at -1). Example output is shown below:

Partition type? primary/extended? primary
File system type? [ext2] fat32
Start? 1
End? -1
(parted): set 1 boot on

Sets the boot flag for this partition.

(parted): set 1 lba on

Sets the lba (Linear Block Addressing) flag for this partition.

(parted): print

Displays the current settings for the new partition. Example output is shown below:

Model: Lexar, Inc. USBdisk (scsi)
Disk /dev/sdb: 1031MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Minor   Start   End     Size    Type     Filesystem  Flags
 1      16.4kB  931MB   1031MB  primary  fat32       boot, lba
(parted)
(parted): quit

Quits the parted utility.

Navigate to the Syslinux mbr directory:

# cd path/mbr

Where path is the folder to which you extracted Syslinux.

Locate the Syslinux master boot record file mbr.bin in the mbr directory and write it to the disk using the following command:

# cat mbr.bin > /dev/sdX

Where X is the drive letter for the USB flash drive (for example, /dev/sda or /dev/sdb).

Navigate to the Syslinux unix directory:

# cd path/unix

Where path is the folder to which you extracted Syslinux.

Note - For later versions of Syslinux, the unix directory might be replaced with a linux directory. If so, replace the unix directory name with linux.

From the Syslinux unix directory, enter the following command:

# ./syslinux /dev/sdX1

Where X is the drive letter for the USB flash drive (for example, /dev/sda or /dev/sdb), and 1 indicates the first partition.

Note - In the next step you will need to specify the mount point. If autofs is running, it might have auto–mounted the drive partition to some other mount point. If this happens, unmount it by entering the command:

umount /dev/sdX1

Mount the drive to a mount point by entering the command:

# mount -t vfat /dev/sdX1 /mnt

Where X is the drive letter for the USB flash drive (for example, /dev/sda or /dev/sdb), and 1 indicates the first partition. For this example, the mount point is /mnt.

Extract the contents of the SIA-version.zip archive file to the USB flash drive by entering the following command:

# unzip -q -d /mnt ~/path/SIA-version.zip -x “source/*”

Where path represents the path to the directory where the .zip file is located, and version represents the SIA version number. The “source/*” parameter excludes the any source files from the extraction to save time and disk space.

Unmount the USB flash drive:

# umount /mnt

Remove the flash drive from client machine.

The USB flash drive is now ready to boot SIA.




https://thornelabs.net/2013/06/10/create-a-bootable-windows-7-usb-drive-in-linux.html
http://www.cyberciti.biz/faq/howto-format-create-linux-filesystem/
http://unix.stackexchange.com/questions/205737/fdisk-l-output-what-are-disk-label-type-and-disk-identifier
http://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line
https://www.mediawiki.org/wiki/Alternative_parsers

https://docs.python.org/2/library/io.html

https://docs.python.org/2/install/
