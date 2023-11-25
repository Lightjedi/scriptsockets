import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.74', 999)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexión
    print('esperando conexión')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        
        # Recibe datos en pequeñas tramas y retrasmitiéndolas
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('regresando los datos al cliente')
                connection.sendall(data)
            else:
                print('no hay datos desde', client_address)
                break
            
    finally:
        # Limpiando la conexión
        print("Cerrando esta conexión")
        connection.close()