# coding: utf-8

import socket
import os.path

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

def create_socket():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(1)

    return server 

def get_file_name(request):
    headers = request.split('\n')
    filename = headers[0].split()[1]

    return filename

def send_response(client_connect, file_name):
    if file_name == "/":
        if os.path.isfile("index.html"):
            with open("index.html", "w") as file:
                content = file.read()
                response = "HTTP/1.0 200 OK\n\n" + content 
        else: 
            response = 'HTTP/1.0 200 OK\n\n\n\n\tHello World'
    else:
        try:
            file_name = file_name[1:]
            with open(file_name, "r") as file:
                content = file.read()
                response = "HTTP/1.0 200 OK\n\n" + content
        except FileNotFoundError:
            response = "HTTP/1.0 404 NOT FOUND\n\n OUPS File Not Found"
        
    client_connect.sendall(response.encode())

def handle_connect(server):
    while True:
        client_connect, client_addr = server.accept()
        request = client_connect.recv(1024).decode()

        print("[server] client {} send a request".format(client_addr))

        file_name = get_file_name(request)
        print("GET {}".format(file_name))
        send_response(client_connect, file_name)

        client_connect.close()

if __name__ == "__main__":
    server = create_socket()
    handle_connect(server)