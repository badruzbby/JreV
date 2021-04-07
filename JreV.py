#coded by B4bbyGhost_
#Thanks to Jamet1337 for API
#Recode Not Make You pro :)
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
 
def getList():
	try:
		Glist = raw_input('Masukkan List =>')
	except:
		Glist = input('Masukkan List => ')
	BacA = open(Glist, 'r').read().splitlines()
	for i in BacA:
		print('reverse dari '+i)
		r = requests.get(url+i)
		has = r.json()
		getdata = has['hasil']
		if getdata == 'Gagal Memuat Data/Subdomain Tidak Ditemukan':
			print('Tidak ada hasil dari '+i)
			pass
		elif getdata != 'Gagal Memuat Data/Subdomain Tidak Ditemukan':
			simpan = open('result.txt', 'a').write(getdata)
			print(getdata)
 
 
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
		print('Error disebabkan '+str(e))
 
def Nom2():
	os.system('clear')
	print(Fore.RED+banner)
	getList()
	
 
 
def Pilih():
	try:
		os.system('clear')
		print(Fore.RED+banner)
		print('''
		1. Single site
		2. Mass site
		''')
		pilihan = input('Pilih => ')
		if pilihan == '1' :
			Nom1()
		if pilihan == '2' :
			Nom2()
		if pilihan >= '3':
			print('Disuruh milih diatas malah milih yang lain')
	except Exception as e:
		print('Error Karena '+str(e))
	except KeyboardInterrupt:
		print('User Abort !!!')
 
try:
	print('checking module')
	print('All module installed')
except ModuleNotFoundError as e:
	print('Error '+ e)
	os.system('python -m pip install -r requirements.txt')
Pilih()
