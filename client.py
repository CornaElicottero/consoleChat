import socket

# Установка параметров клиента
HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Порт, на котором сервер прослушивает подключения

# Создание сокета клиента
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # Подключение к серверу
    while True:
        message = input()    # Получение сообщения от клиента
        s.sendall(message.encode()) # Отправка сообщения серверу
        data = s.recv(1024)  # Получение данных от сервера
        print(data.decode()) # Расшифровка данных и вывод на экран