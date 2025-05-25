import socket
# Tworzenie gniazda serwerowego
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Konfiguracja adresu i portu
server_address = ('10.1.206.44', 5678)
server_socket.bind(server_address)
# Nasłuchiwanie na połączenia
server_socket.listen(1) # Nasłuchuj jednego połączenia
print("Czekam na połączenie...")
client_socket, client_address = server_socket.accept()
print(f"Połączono z {client_address}")
# Odbieranie danych od klienta i przesyłanie ich z powrotem
data = client_socket.recv(1024)
print(f"Otrzymane dane: {data.decode('utf-8')}")
client_socket.send(data) # Odsyłanie danych do klienta
# Zamykanie gniazd
client_socket.close()
server_socket.close()