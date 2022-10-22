import socket
import sys
import signal

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 65444))
    while True:
        data, c_address = s.recvfrom(1024)
        data = data.decode()
        print(data)
        s.sendto(str(data).encode(), c_address)

except KeyboardInterrupt:
    s.close()
    sys.exit(signal.SIGINT)
        
