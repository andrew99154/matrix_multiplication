import socket
import json
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",8888))
theMatrix = [[]]
dic = {"resultIndex":1,"value":0}

while True:
    data = client_socket.recv(1024)
    theMatrix = json.loads(data)
    calculate = theMatrix[0][0]*theMatrix[1][1] + theMatrix[0][1]* theMatrix[1][3]
    dic["value"] = calculate
    client_socket.send(json.dumps(dic).encode())