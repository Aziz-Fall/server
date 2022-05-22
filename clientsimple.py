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

def recv_msg(socket):
    end = True 
    while end:
        response = socket.recv(255).decode()
        if response != "":
            end = False 
            print("[server] {}".format(response))
            print("[client] > Close ")
            socket.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        client = connection()
        send_msg(client, sys.argv[1])
        if sys.argv[1] == "fin":
            client.close()
        else:
            recv_msg(client)
    else: 
        print("[-] Less Argument")
