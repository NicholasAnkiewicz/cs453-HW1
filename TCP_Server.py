import socket
import sys
import signal

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 65444))
    s.listen(5)
    c_sock, c_address = s.accept()
    while True:
        recieved = c_sock.recv(1024)
        if not recieved:
            c_sock.close()
            break
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
        c_sock.sendall(str(data).encode())
    s.close()

except KeyboardInterrupt:
    s.close()
    sys.exit(signal.SIGINT)
        
