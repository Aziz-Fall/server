# coding: utf-8 

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 9000))

fin_com = True
while fin_com: 
    socket.listen(5)
    client, addresse = socket.accept()
    print("[server] > {} connected".format(addresse))

    response = client.recv(255)
    if response.decode() == "fin":
        fin_com = False
    elif response != "":
        print("[client] > {}".format(response.decode()))
        response = response.decode().upper()
        client.send(response.encode('utf-8'))
    else:
        print("[server] > No response")

print("[server] > End Connection")
client.close()
socket.close()

