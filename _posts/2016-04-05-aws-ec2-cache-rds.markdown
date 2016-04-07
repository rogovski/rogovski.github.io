---
layout: post
title:  "Creating an EC2 instance with RDS and ElasticCache"
date:   2016-04-05 13:14:00 -0500
categories: infrastructure
description: "How to setup and configure"
---

### Creating a key pair

```bash
chmod 0400 <your-key>.pem
```

### Creating a security group

TODO

http://www.lauradhamilton.com/how-to-set-up-a-nodejs-web-server-on-amazon-ec2

### Configuring the instance to work with a node.js server
```bash
cat /proc/sys/net/ipv4/ip_forward
```
a return value of zero indicates thats ip forwarding is disabled. A 1 means it's enabled.

```bash
sudo vim /etc/sysctl.conf
```
In this file, uncomment this line:

```bash
net.ipv4.ip_forward
```
This will enable ip forwarding. Then, to enable the changes made in sysctl.conf:

```bash
sudo sysctl -p /etc/sysctl.conf
```
Now, let's check that ip forwarding is enabled:

```bash
cat /proc/sys/net/ipv4/ip_forward
```
That should return a 1 now.

set up forwarding from 80 to 8080:
```bash
sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
```
Next, we need to open the Linux firewall to allow connections on port 80:

```bash
sudo iptables -A INPUT -p tcp -m tcp --sport 80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT
```
