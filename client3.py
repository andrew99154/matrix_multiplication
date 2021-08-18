import socket
import json
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",8888))
theMatrix = [[]]
dic = {"resultIndex":2,"value":0}

while True:
    data = client_socket.recv(1024)
    theMatrix = json.loads(data)
    calculate = theMatrix[0][2]*theMatrix[1][0] + theMatrix[0][3]* theMatrix[1][2]
    dic["value"] = calculate
    client_socket.send(json.dumps(dic).encode())