import socket
import sys
import signal
import random

try:
    p = sys.argv[1]
    random.seed(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 65444))
    while True:
        recieved, c_address = s.recvfrom(1024)
        if random.random() <= int(p):
            print(f"{recieved.decode()} -> dropped")
            pass
        data = recieved.decode()
        data = data.split(" ")
        if ((["+", "-", "*", "/"].count(data[0]) == 0)):
            data = "620 -1"
        elif (not data[1].strip("-").isdigit()):
            data = "630 -1"
        elif (not data[2].strip("-").isdigit()):
            data = "630 -1"
        elif (data[2] == "0" and data[0] == "/"):
            data = "630 -1"
        else:
            if (data[0] == "+"):
                data = int(data[1]) + int(data[2])            
            elif data[0] == "-":
                data = int(data[1]) - int(data[2])
            elif data[0] == "*":
                data = int(data[1]) * int(data[2])
            elif data[0] == "/":
                data = int(data[1]) / int(data[2])
            data = "200 " + str(data)
        print(recieved.decode(), "->", data)
        s.sendto(str(data).encode(), c_address)

except KeyboardInterrupt:
    s.close()
    sys.exit(signal.SIGINT)