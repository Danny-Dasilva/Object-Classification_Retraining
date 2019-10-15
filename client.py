import socket
from PIL import Image
CHUNK_SIZE = 8 * 1024

sock = socket.socket()
sock.connect(('localhost', 12345))
chunk = sock.recv(CHUNK_SIZE)
test = []
while chunk:
    chunk = sock.recv(CHUNK_SIZE)
    print(chunk)

# image = Image.frombytes('RGBA', (128,128), chunk, 'raw')
# image.show()
sock.close()
