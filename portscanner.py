#!/bin/python3

import sys
import socket
from datetime import datetime 

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to Ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: portscanner.py <ip> ")
print("*"*50)
print("scanning target:" + target)
print("Time Started :"+ str(datetime.now()))
print("*"*50)
#Port
try:
	for port in range(50,90):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s. connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open ")
		s.close()
	
except KeyboardInterrupt:
	print("\n Exiting program....")
	sys.exit()
except socket.error:
	print("Could not connect to the server")
	sys.exit()
