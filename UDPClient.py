from socket import *

clientPort = 50001  # İstemci portu
serverIP = '127.0.0.1'  # Sunucu IP adresi
serverPort = 50000  # Sunucu portu
clientSocket = socket(AF_INET, SOCK_DGRAM)  # UDP soketi oluştur

clientSocket.bind(('', clientPort))  # İstemci portunu belirle, aksi takdirde otomatik atanır

while True:
    message = input('Metni giriniz: Çıkış için (son) yazınız\n')  # Kullanıcıdan metin al
    if message == 'son':
        break
    message = message.encode()  # Metni baytlara çevir
    serverAddress = (serverIP, serverPort)  # Sunucu adresi
    clientSocket.sendto(message, serverAddress)  # Mesajı sunucuya gönder
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Sunucudan gelen cevabı al
    print(f"Bağlantı kurulan istemci adresi: {serverAddress}")  # Sunucunun adresini yazdır
    modifiedMessage = modifiedMessage.decode()  # Baytları metne dönüştür
    print(modifiedMessage)  # Mesajı yazdır

clientSocket.close()  # Soketi kapat
