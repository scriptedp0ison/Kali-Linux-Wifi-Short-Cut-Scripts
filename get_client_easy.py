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

