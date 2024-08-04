# TCP ve UDP İletişimi

Bu proje, TCP ve UDP protokollerini kullanarak istemci-sunucu iletişimini gösteren Python kod örneklerini içerir. Proje, temel ağ programlama konularında bilgi edinmenizi sağlar ve TCP ve UDP iletişimi hakkında pratik örnekler sunar.

## İçindekiler
- [Proje Açıklaması](#proje-a%C3%A7%C4%B1klamas%C4%B1)
- [Kullanılan Kodlar](#kullan%C4%B1lan-kodlar)
- [Kodların Çalıştırılma Sırası](#kodlar%C4%B1n-%C3%A7al%C4%B1%C5%9Ft%C4%B1r%C4%B1lma-s%C4%B1ras%C4%B1)
- [Kurulum ve Kullanım](#kurulum-ve-kullan%C4%B1m)

## Proje Açıklaması
Bu proje, TCP ve UDP protokollerini kullanarak istemci ve sunucu uygulamaları oluşturur. TCP ve UDP üzerinden veri iletimi ve alımı ile ilgili temel anlayış sağlar.

## Kullanılan Kodlar
- **TCPClient.py**: TCP istemci uygulaması. Sunucuya bağlanır, mesaj gönderir ve sunucudan gelen yanıtı alır.
- **TCPServer.py**: TCP sunucu uygulaması. İstemcilerden gelen bağlantıları kabul eder, mesajları alır ve yanıt verir.
- **UDPClient.py**: UDP istemci uygulaması. Sunucuya mesaj gönderir ve yanıt alır.
- **UDPServer.py**: UDP sunucu uygulaması. İstemcilerden gelen mesajları alır ve yanıt verir.

## Kodların Çalıştırılma Sırası
1. **TCP Sunucu Kodu (TCPServer.py)**: İlk olarak TCP sunucu kodunu çalıştırarak sunucuyu başlatın. Sunucu, istemcilerden gelen bağlantıları ve mesajları kabul etmeye hazır olacaktır.
    ```bash
    python TCPServer.py
    ```

2. **TCP İstemci Kodu (TCPClient.py)**: TCP sunucusu başlatıldıktan sonra, TCP istemci kodunu çalıştırın. Bu kod, sunucuya bağlanır, mesaj gönderir ve yanıt alır.
    ```bash
    python TCPClient.py
    ```

3. **UDP Sunucu Kodu (UDPServer.py)**: UDP sunucu kodunu çalıştırarak UDP sunucusunu başlatın. Sunucu, istemcilerden gelen mesajları almaya hazır olacaktır.
    ```bash
    python UDPServer.py
    ```

4. **UDP İstemci Kodu (UDPClient.py)**: UDP sunucusu başlatıldıktan sonra, UDP istemci kodunu çalıştırın. Bu kod, sunucuya mesaj gönderir ve yanıt alır.
    ```bash
    python UDPClient.py
    ```

## Kurulum ve Kullanım
1. Python'un en son sürümünü [buradan](https://www.python.org/downloads/) indirin ve kurun.

2. Bu repository'yi klonlayın:
    ```bash
    git clone https://github.com/SukriyeKaramann/Python-Socket-Programming.git
    ```

3. Proje dizinine gidin ve gerekli Python paketlerini yükleyin (gerekiyorsa).

4. İstemci ve sunucu kodlarını çalıştırarak ağ iletişimini test edin.
