import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 65444))
    s.listen()
    c_sock, c_address = s.accept()
    print("Connected: ", c_address)
    while True:
        data = c_sock.recv(1024)
        if not data:
            c_sock.close()
            break
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
            data[1] = int(data[1])
            data[2] = int(data[2])
            match data[0]:
                case "+":
                    data = data[1] + data[2]
                case "-":
                    data = data[1] - data[2]
                case "*":
                    data = data[1] * data[2]
                case "/":
                    data = data[1] / data[2]
        c_sock.sendall(str(data).encode())
    s.close()
except KeyboardInterrupt:
    c_sock.close()
    s.close()

        
