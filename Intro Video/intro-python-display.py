import sys,time,random, string
from os import system, name 
from time import sleep
from colorama import Fore, Back, Style, init

init()

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def slow_type(t,speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*speed/100)
    print ('')

def id_generator(chars=string.ascii_uppercase + string.digits):
	for x in range(350):
		sys.stdout.write("\033[K")
		size = random.randrange(6, 23, 2)
		#print('\r', end='')
		print('\t0x' + ''.join(random.choice(chars) for _ in range(size)) + "h",end='\r')
		sleep(0.05)

def countdown(n):
	while n > 0:
		sys.stdout.write("\033[K")
		print('\r Starting in: ' + str(n), end='')
		time.sleep(1)
		n = n - 1
	print("")

clear()
start_time = time.time()
countdown(15)
clear()
sleep(3)
slow_type(Fore.WHITE + """    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 Hacker\'s Arsenal 
                     Episode 0x00
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        { Kali on Windows10 }\n""", 1)
sleep(5)
slow_type(Fore.WHITE + "[+] Identifying User",1)
sleep(5)
slow_type(Fore.WHITE + "[!] Network IP:" + Fore.RED +" Fail " + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLACK + "TOR NODE detected" + Style.RESET_ALL+ "]",1)
sleep(5)
slow_type(Fore.WHITE + "[+] Enabling USB DEBUG [Glitch:" + Fore.GREEN + " Enabled" + Fore.WHITE + "])", 1)
id_generator()
slow_type(Fore.WHITE + "[+] WEBCAM found (Memory addr:" + Style.BRIGHT + Fore.BLACK + " C8DE_2300h" + Style.RESET_ALL + ")", 1)
#sleep(5)
#slow_type(Fore.WHITE + "[+] Video Frames captured", 1)
sleep(5)
slow_type("[+] Using neuralnet to identify user", 1)
sleep(5)
slow_type("[+] User Identity confirmed:", 1)
slow_type("    -   UserName:" + Fore.GREEN + " @hevnsnt", 1)
slow_type(Fore.WHITE + "    - Confidence: " + Fore.GREEN + "99.23% Accuracy",1)
slow_type(Fore.WHITE + "    -     Access: " + Fore.GREEN + "Granted",1)
sleep(3)
slow_type(Fore.WHITE + "[+] Starting Hacker's Arsenal\n", 1)
print("--- %s seconds ---" % (time.time() - start_time))
input("")
