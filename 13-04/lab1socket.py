import socket

# Tworzenie gniazda klienckiego
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tworzenie gniazda serwerowego
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5678) # Przykładowy adres i port
server_socket.bind(server_address)

server_socket.listen(x) # Nasłuchuj maksymalnie x połączeń
client_socket, client_address = server_socket.accept() # akceptowanie połaczań

server_address = ('localhost', 5678)
client_socket.connect(server_address)

#Wysyłanie danych
client_socket.send(b'Hello, server!')
#Odbieranie danych
data = client_socket.recv(1024) # Odbierz maksymalnie 1024 bajty danych

client_socket.close()
server_socket.close()