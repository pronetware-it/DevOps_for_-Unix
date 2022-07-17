## Task-1 ##
1. Create virtual machines connection according to figure 1:




2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure all network
   interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

### Setting interfaces VM 1 ###

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

### Enable forward ###

By default, transit traffic is disabled

- `cat /proc/sys/net/ipv4/ip_forward`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/3.gif)

- `sudo nano /etc/sysctl.conf`

To turn on, edit the line `#net.ipv4.ip_forward=1` on `net.ipv4.ip_forward=1`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/4.gif)

So that the changes made to enter into force

- `sudo sysctl -p /etc/sysctl.conf`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/5.gif)

### Setting iptables ###

- `sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -m state --state RELATED,ESTABLISHED -j ACCEPT`
- `sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT`

- `sudo iptables -L -v --line-numbers`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/6.gif)

### Enable MASQUERADE ###

- `sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE`

- `sudo iptables -t nat -L -v --line-numbers`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/7.gif)

3. Check the route from VM2 to Host.


4. Check the access to the Internet, (just ping, for example, 8.8.8.8).


5. Determine, which resource has an IP address 8.8.8.8.


6. Determine, which IP address belongs to resource epam.com.


7. Determine the default gateway for your HOST and display routing table.


8. Trace the route to google.com.
