import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando el socket al puerto donde el servidor está escuchando
server_address = ('192.168.1.74', 999)
print('conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    # Envío de datos
    message = b'Es un mensaje muy grande pero sera transmitido en secciones de 16'
    print('enviando {!r}'.format(message))
    sock.sendall(message)
    
    # Verificación de respuesta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received +=len(data)
        print('recibido {!r}'.format(data))
        
finally:
    print('cerrando socket')
    sock.close()
