# coding: utf-8 

from doctest import FAIL_FAST
from gc import set_debug
from pydoc import cli
import socket
import os.path

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", 9000))

def read_file(name):
    with open(name, 'r') as file:
        return file.readlines()

def get_file_content(path):        
    if os.path.isfile(path):
            file_content = read_file(path)
            return file_content
    else: 
        print("[server] File <{}> does not exist".format(path)) 

    return "FILE_ERROR"

def send_file_content(client, content):
    if "ERROR" in content:
        client.send("ERROR".encode('utf-8'))
    else:
        content = ''.join(content)
        client.send(content.encode('utf-8'))

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
        file_content = get_file_content(response.decode())
        send_file_content(client, file_content)
    else:
        print("[server] > No response")

print("[server] > End Connection")
client.close()
socket.close()

