import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(socket.gethostname(), 65444)
s.listen()