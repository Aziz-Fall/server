# coding: utf-8

import socket
import sys 

def connection():
    client = ("localhost", 9000)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(client)
    print("[client] > Connection on port {}".format(client[1]))
    return s

def send_msg(socket, msg):
    if msg != "":
        socket.send(msg.encode('utf-8'))
    elif msg == "fin":
        socket.close()

def recv_msg(socket, name_file):
    end = True 
    while end:
        file_content = socket.recv(1024).decode()
        if "ERROR" not in file_content:
            end = False 
            with open(name_file, 'w') as file:
                file.write(file_content)
            print("[client] > Close ")
            socket.close()
        else:
            end = False
            print("[client] > Close ")
            socket.close()

if __name__ == "__main__":
    if len(sys.argv) == 2 and len(sys.argv[1]):
        client = connection()
        send_msg(client, sys.argv[1])
        if sys.argv[1] == "fin":
            client.close()
        else:
            recv_msg(client, sys.argv[1])
    else: 
        print("[-] Less Argument")
