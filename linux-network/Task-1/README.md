## Task-1 ##
1. Create virtual machines connection according to figure 1:




2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure all network
   interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

- `sudo cp /etc/netplan/00-installer-config.yaml 01-netcfg.yaml`
- `sudo nano /etc/netplan/01-netcfg.yaml`

```# This is the network config written by 'subiquity'
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: false
      addresses: [10.15.15.1/24]
```
- `sudo netplan try`
- `sudo netplan apply`


![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/1.gif)






