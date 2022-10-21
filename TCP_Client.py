import socket
import os

curDirectory = os.path.dirname(__file__)
fullPath = os.path.join(curDirectory, "sample_data.txt")
input_lines = []
with open(fullPath, 'r') as file:
    for line in file:
        input_lines.append(line)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 65444))
for line in input_lines:
    line = line.strip('\n')
    print("Sending ", line, "to 127.0.0.1")
    s.sendall((line).encode())
    data = s.recv(1024)
    data = data.decode()
    print(data)