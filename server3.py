import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}")

sock.bind(server_address)

sock.listen(1)

# クライアントからの接続待ち
while True:
    connection, client_address = sock.accept()
    try:
        print(f"connection from {client_address}")

        # サーバが新しいデータを待つ
        while True:
            data = connection.recv(4096)

            data_str = data.decode('utf-8')
            print(f"Recieved message : {data_str}")

            if data:
                # データ処理
                response = "住所：" + data_str

                connection.sendall(response.encode())
            else:
                print(f"no data from {client_address}")
                break

    finally:
        print("Closing connection")
        connection.close()