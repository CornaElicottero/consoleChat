import socket

# Установка параметров сервера
HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Порт, на котором сервер будет прослушивать подключения

# Создание сокета сервера
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))   # Привязка сокета к адресу и порту
    s.listen()             # Прослушивание входящих подключений
    conn, addr = s.accept() # Ожидание подключения клиента
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # Получение данных от клиента
            if not data:           # Если данные не получены, завершить соединение
                break
            print(data.decode())   # Расшифровка данных и вывод на экран
            message = input()      # Получение сообщения от сервера
            conn.sendall(message.encode()) # Отправка сообщения клиенту