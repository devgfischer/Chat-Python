import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('192.168.64.91', 8080)) # setar o servidor com base no IPv4 da sua máquina
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n') # retorna uma msg de erro 

    while True:
        client, addr = server.accept()
        clients.append(client)

        namefiles = client.recv(1024).decode()

        thread = threading.Thread(target=messagesTreatment, args=[client]) # aqui iniciamos o tratamento da mensagem.
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break

def broadcast(msg, client): # aqui que ele faz a transmissão em tempo real.
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

main()
