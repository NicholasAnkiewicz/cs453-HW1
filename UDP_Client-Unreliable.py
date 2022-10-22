from cmath import exp
from logging import exception
import socket
import os
import sys
import time

curDirectory = os.path.dirname(__file__)
fullPath = os.path.join(curDirectory, sys.argv[1])
input_lines = []
with open(fullPath, 'r') as file:
    for line in file:
        input_lines.append(line)

d=0.1
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for line in input_lines:
    line = line.strip('\n')
    
    while d < 2:
        s.sendto((line).encode(), ("127.0.0.1", 65444))
        data, s_address = s.recvfrom(1024)
        time.sleep(d)
        if data:
            if d > 2:
                raise exception("Request timed out: the server is dead")    
            d = d * 2
            print("Request timed out: resending")
        else:
            break
    data = data.decode()
    data = data.split(" ")
    if data[0] == "200":
        print("Result is",data[1])
    if data[0] == "620":
        print(f"Error {data[0]}: Invalid OC")
    if data[0] == "630":
        print(f"Error {data[0]}: Invalid operands")