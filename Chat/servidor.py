import socket
import threading

def handle_client(client_socket, addr, clients):
    print(f"Conexión establecida con: {addr}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"{addr} dice: {message}")

            # Reenviar el mensaje a todos los demás clientes
            for c in clients:
                if c != client_socket:
                    c.send(f"{addr} dice: {message}".encode('utf-8'))
    except ConnectionResetError:
        print(f"Conexión cerrada por {addr}")
    finally:
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor iniciado en {host}:{port}")

    clients = []
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr, clients))
        thread.start()

if __name__ == "__main__":
    start_server()