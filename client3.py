import socket
import sys
from faker import Faker

fake = Faker('jp-JP')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print(f"Connectig to {server_address}")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = fake.address()
    sock.sendall(message.encode())

    sock.settimeout(2)

    try:
        while True:
            data = sock.recv(4096).decode('utf-8')

            if data:
                print(f"Server response: {data}")
            else:
                break
    
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
