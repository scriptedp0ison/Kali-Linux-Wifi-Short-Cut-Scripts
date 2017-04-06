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
