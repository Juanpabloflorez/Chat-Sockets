import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print("\n" + data.decode('utf-8'))
        except:
            break

def start_client():
    host = 'localhost'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Conectado al servidor en {host}:{port}")

    # Hilo para recibir mensajes
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("Tú: ")
        if message.lower() == 'salir':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_client()