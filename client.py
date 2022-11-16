import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('192.168.1.106', 8080)) # setar o IPv4 do servidor
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n') # imprime uma mensagem de erro caso o IPv4 não for o correto.

    username = input('Usuário> ')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

'''Na linha 4 até a 18 startamos duas thread, 
    uma para receber a mensagem e outra para mandar a mensagem'''

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8') # usamos essa linha para conseguirmos usar caracteres especiais no terminal
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def sendMessages(client, username): # parte onde a mensagem é enviada pelo client
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return

main()
