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
	print('[+] Compiling system arguments,,,')
	time.sleep(1)
	print('[+] Executing system arguments...')
	time.sleep(2)
	launch_attack = 'airodump-ng -c {} --bssid {} {}'.format(sys.argv[2], sys.argv[4], sys.argv[6])
	subprocess.call(launch_attack, shell=True)
if sys.argv[1] == '-h':
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

