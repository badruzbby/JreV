import requests
import os
from colorama import init
from colorama import Fore
url = 'http://jamet1337.ml/api/revip.php?url='
init(autoreset=True)

banner = '''

 ▄▄▄██▀▀▀██▀███  ▓█████ ██▒   █▓
   ▒██  ▓██ ▒ ██▒▓█   ▀▓██░   █▒
   ░██  ▓██ ░▄█ ▒▒███   ▓██  █▒░
▓██▄██▓ ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░   DragonXploiter Team
 ▓███▒  ░██▓ ▒██▒░▒████▒  ▒▀█░     Thanks to Jamet1337
 ▒▓▒▒░  ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  
 ▒ ░▒░    ░▒ ░ ▒░ ░ ░  ░  ░ ░░  
 ░ ░ ░    ░░   ░    ░       ░░  
 ░   ░     ░        ░  ░     ░  
                            ░   
                            
               Coded by B4bbyGhost_
'''

def Nom1():
	try:
	    os.system('clear')
	    print(Fore.RED+banner)
	    print('single Site rev')
	    site = input('Site => ')
	    r = requests.get(url+site)
	    has = r.json()
	    data = has['hasil']
	    print('\n=======Result=======')
	    print(data)
	except KeyboardInterrupt:
		print('User Abort !!')
	except Exception as e:
		print('Error disebabkan'+str(e))

def Nom2():
	os.system('clear')
	print(Fore.RED+banner)
	print('Coming soon !!')
	
	
def Pilih():
	try:
		os.system('clear')
		print(Fore.RED+banner)
		print('''
		1. Single site
		2. Mass site (coming soon)
		''')
		pilihan = input('Pilih => ')
		if pilihan == '1' :
			Nom1()
		if pilihan == '2' :
			Nom2()
		if pilihan >= '3':
			print('Disuruh milih diatas malah milih yang lain')
	except Exception as e:
		print(e)
	except KeyboardInterrupt:
		print('User Abort !!!')
		
Pilih()