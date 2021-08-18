import socket
import json
import threading
import time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",8888))
server_socket.listen(4)
matrix = [[],[]]
client_info = []
amounts_of_threads = 0
resultMatrix = [0,0,0,0]

def thread_socket(theClient):
    while True:
        try:
            data = json.loads(theClient.recv(1024)) #dictionary { resultIndex , value }
            resultMatrix[data["resultIndex"]] = data["value"]
        except:
            break

for i in range(4):
    client, addr = server_socket.accept()
    client_info.append(client)
    amounts_of_threads += 1
    print ("amounts of threads: ",amounts_of_threads)
    theThread = threading.Thread(target=thread_socket,args=(client,))
    theThread.start()

while True:
    for i in range(2):
        matrixTmp = input()
        matrix[i] = (list(map(int,matrixTmp.split(" "))))
    sendMatrix = json.dumps(matrix).encode()
    for i in range(4):
        client_info[i].send(sendMatrix)
    time.sleep(0.5)
    print(resultMatrix)