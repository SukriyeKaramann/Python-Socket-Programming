from socket import *

serverPort = 50000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connected to {addr}")
    message = connectionSocket.recv(2048)  # 2 KB boyutunda veri alır
    message = message.decode()  # Bayt dizisini metne dönüştür
    modifiedMessage = message.upper()  # Mesajı büyük harfe dönüştür
    modifiedMessage = modifiedMessage.encode()  # Büyük harfe dönüştürülmüş mesajı bayt dizisine çevir
    connectionSocket.send(modifiedMessage)  # Dönüştürülmüş mesajı istemciye gönder
    connectionSocket.close()  # Bağlantıyı kapat
