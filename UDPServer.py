from socket import *

serverPort = 50000  # Sunucu portu
serverSocket = socket(AF_INET, SOCK_DGRAM)  # UDP soketi oluştur
serverSocket.bind(('', serverPort))  # Sunucu portunu belirle

print('Sunucu mesaj alımı için hazır')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # İstemciden gelen mesajı al
    print(f"Bağlantı kurulan istemci adresi: {clientAddress}")  # İstemci adresini yazdır
    message = message.decode()  # Baytları metne dönüştür
    modifiedMessage = message.upper()  # Mesajı büyük harfe dönüştür
    modifiedMessage = modifiedMessage.encode()  # Büyük harfe dönüştürülmüş mesajı baytlara çevir
    serverSocket.sendto(modifiedMessage, clientAddress)  # Mesajı istemciye gönder
