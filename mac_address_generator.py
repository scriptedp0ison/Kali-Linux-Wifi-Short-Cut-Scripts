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
