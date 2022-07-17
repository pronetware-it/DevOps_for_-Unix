## Task-2 ##
Configuring DHCP, DNS servers
and dynamic routing using OSPF protocol

1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal,
VM2, VM3 – internal only interfaces.


2. Install and configure DHCP server on VM1. (3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER).
You should use at least 2 of them.

- `sudo apt install isc-dhcp-server`
- `sudo nano /etc/default/isc-dhcp-server`
- `sudo service isc-dhcp-server restart`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/1.gif)

- `sudo cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.bak`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/2.gif)

- `sudo nano /etc/dhcp/dhcpd.conf`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/4.gif)

- `sudo service isc-dhcp-server restart`
- `sudo service isc-dhcp-server status`

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/3.gif)


3. Check VM2 and VM3 for obtaining network addresses from DHCP server.

- Check dhcp list on VM1

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/dhcp-list.gif)

- Chech dhcp in VM2

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/ch-vm2-dhcp.gif)

- Chech dhcp in VM3

![image](https://github.com/pronetware-it/DevOps_for_Unix/blob/main/linux-network/Task-2/ch-vm3-dhcp.gif)



4. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. (You can
use DNSMASQ, BIND9 or something else).

- `sudo apt install bind9`
- `sudo nano /etc/bind/named.conf.options`

- `sudo named-checkconf`
- `sudo systemctl restart bind9`

5. Check VM2 and VM3 for gaining access to DNS server (naming services).




6. ***Using the scheme which follows, configure dynamic routing using OSPF protocol.
