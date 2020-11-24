import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('127.0.0.1', 3000))

cmd = 'GET http://127.0.0.1/image HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

picture = b""

while True:
    data = mysock.recv(5120)
    
    if len(data) < 1:
        break
    
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")

print(picture[:pos].decode())   #it will print the header of the file

picture = picture[pos+4:]   #it will trim the header and leave the 4 characters '\r\n\r\n' ans assign the remaining characters to the picture variable

fhand = open("downloaded_image.jpg", "wb")      # 'wb' means write in byte mode

fhand.write(picture)

fhand.close()