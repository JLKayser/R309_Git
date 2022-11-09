import socket


def client():
    host = socket.gethostname()
    port = 5000  # Port du socket server

    client_socket = socket.socket()
    client_socket.connect((host, port))  # conneter au server

    message = input("   -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # envoie le message
        data = client_socket.recv(1024).decode()  # recois les reponse

        print('Reçu du serveur: ' + data)

        message = input("   -> ")

    client_socket.close()  # Fermer la connexion


if __name__ == '__main__':
    client()