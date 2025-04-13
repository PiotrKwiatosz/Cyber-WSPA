import socket
# Tworzenie gniazda klienckiego
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Konfiguracja adresu i portu serwera
server_address = ('10.1.206.44', 5678)
# Nawiązywanie połączenia z serwerem
client_socket.connect(server_address)
# Wysyłanie danych do serwera
message = "Hello, server!"
client_socket.send(message.encode('utf-8'))
# Odbieranie danych od serwera
data = client_socket.recv(1024)
print(f"Odpowiedź serwera: {data.decode('utf-8')}")
# Zamykanie gniazda
client_socket.close()