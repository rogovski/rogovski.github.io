---
layout: post
title:  "UBUNTU SERVER"
date:   2016-05-14 13:14:00 -0500
categories: infrastructure
description: "How to setup and configure"
---

sudo apt-get install openssh-server 

sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
sudo chmod a-w /etc/ssh/sshd_config.factory-defaults

sudo nano /etc/ssh/sshd_config
# change auth mode if needed

sudo systemctl restart ssh
sudo shutdown -P now

http://askubuntu.com/questions/64915/how-do-i-install-ubuntu-on-a-virtualbox-client-from-an-iso-image