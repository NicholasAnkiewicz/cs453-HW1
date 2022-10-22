import socket
import os
import sys


curDirectory = os.path.dirname(__file__)
fullPath = os.path.join(curDirectory, sys.argv[-1])
input_lines = []
with open(fullPath, 'r') as file:
    for line in file:
        input_lines.append(line)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 65444))
for line in input_lines:
    line = line.strip('\n')
    s.sendall((line).encode())
    data = s.recv(1024)
    data = data.decode()
    data = data.split(" ")
    if data[0] == "200":
        print("Result is", data[1])
    if data[0] == "620":
        print(f"Error {data[0]}: Invalid OC")
    if data[0] == "630":
        print(f"Error {data[0]}: Invalid operands")