import socket
import sys
import signal

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 65444))
    while True:
        data = s.recvfrom(1024)
        c_address = data[1]
        data = data[0]
        data = data.decode()
        print(data)
        data = data.split(" ")
        if len(data) != 3 or len(data[0]) != 1:
            data = "-1"
        elif ((["+", "-", "*", "/"].count(data[0]) == 0)):
            data = 620
        elif (not data[1].strip("-").isdigit()):
            data = 630
        elif (not data[2].strip("-").isdigit()):
            data = 630
        elif (data[2] == "0" and data[0] == "/"):
            data = 630
        else:
            if (data[0] == "+"):
                data = int(data[1]) + int(data[2])            
            elif data[0] == "-":
                data = int(data[1]) - int(data[2])
            elif data[0] == "*":
                data = int(data[1]) * int(data[2])
            elif data[0] == "/":
                data = int(data[1]) / int(data[2])
        s.sendto(str(data).encode(), c_address)

except KeyboardInterrupt:
    s.close()
    sys.exit(signal.SIGINT)
        
