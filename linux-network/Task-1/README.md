## Task-1 ##
1. Create virtual machines connection according to figure 1:

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/sc-net-1.png)

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/sc-net-2.png)


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

### Setting interfaces VM 2 ###

- `sudo cp /etc/netplan/00-installer-config.yaml 01-netcfg.yaml`
- `sudo nano /etc/netplan/01-netcfg.yaml`

```# This is the network config written by 'subiquity'
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: false
      addresses: [10.15.15.2/24]
      gateway4: 10.15.15.1
      nameservers:
          addresses: [8.8.8.8, 8.8.4.4]
```

- `sudo netplan try`
- `sudo netplan apply`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/8.gif)

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

### Save iptables ###

- `sudo apt install iptables-persistent`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/save-iptables.gif)

### Enable MASQUERADE ###

- `sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE`

- `sudo iptables -t nat -L -v --line-numbers`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/7.gif)

3. Check the route from VM2 to Host.

- `traceroute 192.168.55.1`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/14.gif)


4. Check the access to the Internet, (just ping, for example, 8.8.8.8).

- `ping 8.8.8.8`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/10.gif)


5. Determine, which resource has an IP address 8.8.8.8.

- `nslookup 8.8.8.8`

```
8.8.8.8.in-addr.arpa    name = dns.google.
Authoritative answers can be found from:
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/11.gif)


6. Determine, which IP address belongs to resource epam.com.

- `nslookup epam.com`

```Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   epam.com
Address: 3.214.134.159
```

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/12.gif)

7. Determine the default gateway for your HOST and display routing table.

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/sc-net-3.png)

```C:\Users\Project>route print
===========================================================================
Список интерфейсов
  2...28 d2 44 49 a9 dd ......Realtek PCIe FE Family Controller
  9...0a 00 27 00 00 09 ......VirtualBox Host-Only Ethernet Adapter
  3...fc f8 ae 1f cd be ......Microsoft Wi-Fi Direct Virtual Adapter
  5...fe f8 ae 1f cd bd ......Microsoft Wi-Fi Direct Virtual Adapter #2
 11...fc f8 ae 1f cd bd ......Intel(R) Wireless-N 7260
 12...fc f8 ae 1f cd c1 ......Bluetooth Device (Personal Area Network)
  1...........................Software Loopback Interface 1
===========================================================================

IPv4 таблица маршрута
===========================================================================
Активные маршруты:
Сетевой адрес           Маска сети      Адрес шлюза       Интерфейс  Метрика
          0.0.0.0          0.0.0.0      192.168.1.1     192.168.1.55     45
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    331
      192.168.1.0    255.255.255.0         On-link      192.168.1.55    301
     192.168.1.55  255.255.255.255         On-link      192.168.1.55    301
    192.168.1.255  255.255.255.255         On-link      192.168.1.55    301
     192.168.56.0    255.255.255.0         On-link      192.168.56.1    281
     192.168.56.1  255.255.255.255         On-link      192.168.56.1    281
   192.168.56.255  255.255.255.255         On-link      192.168.56.1    281
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    331
        224.0.0.0        240.0.0.0         On-link      192.168.56.1    281
        224.0.0.0        240.0.0.0         On-link      192.168.1.55    301
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    331
  255.255.255.255  255.255.255.255         On-link      192.168.56.1    281
  255.255.255.255  255.255.255.255         On-link      192.168.1.55    301
===========================================================================
```

8. Trace the route to google.com.

- `traceroute google.com`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-1/13.gif)
