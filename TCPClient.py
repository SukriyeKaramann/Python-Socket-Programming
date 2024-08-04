from socket import *

serverName = '127.0.0.1'  # Sunucu IP adresi
serverPort = 50000  # Sunucu port numarası
clientPort = 60001  # İstemci port numarası (Opsiyonel)

# İstemci soketini oluştur
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', clientPort))  # Opsiyonel: İstemci portunu belirleme
clientSocket.connect((serverName, serverPort))  # Sunucuya bağlan

while True:
    message = input("Metin giriniz: (Çıkış için 'exit' yazın)\n")
    if message.lower() == 'exit':
        break  # Döngüyü sonlandır

    message = message.encode()  # Mesajı baytlara dönüştür
    clientSocket.send(message)  # Mesajı sunucuya gönder
    modifiedMessage = clientSocket.recv(2048)  # Sunucudan cevabı al
    modifiedMessage = modifiedMessage.decode('utf-8')  # Baytları metne dönüştür
    print(modifiedMessage)  # Cevabı yazdır

clientSocket.close()  # Soketi kapat
