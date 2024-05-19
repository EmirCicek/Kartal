import RPi.GPIO as GPIO
import socket
import time

def lamba_ac():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    print("Lamba Açıldı")

def lamba_kapat():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    print("Lamba Kapatıldı")

def cleanup_gpio():
    GPIO.cleanup()

#lamba_acik = False

def start_client():
    counter = 0
    # Client bilgileri
    host = '192.168.1.21'
    port = 12345
#     host = "8.tcp.ngrok.io"
#     port = 13257
    while True:
        try:
            print(f"Bağlanıyor: {host}:{port}")

            # Client socket oluştur
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            # Server'dan gelen veriyi al
            data = client_socket.recv(1024).decode()

            # Gelen veriye göre fonksiyon çalıştır
            if data == "1":
                lamba_ac()
  #              lamba_acik = True
            elif data == "2":
                lamba_kapat()
   #             cleanup_gpio()
                lamba_acik = False
            # Bağlantıyı kapat
            client_socket.close()
            counter += 1
            break  # Bağlandıktan sonra döngüyü kır

        except ConnectionRefusedError:
            # Server henüz başlamamış, tekrar dene
            print("Server'a bağlanılamadı, tekrar deneniyor...")
            time.sleep(1)  # 1 saniye bekle ve tekrar dene
            counter += 1
#            if lamba_acik:
#              lamba_ac()
#            else:
#              lamba_kapat()
#              cleanup_gpio()


        finally:
            print("Finally bölümü")
            #cleanup_gpio()  # GPIO pinlerini temizle
 #           if lamba_acik:
#              lamba_ac()
 #           else:
 #             lamba_kapat()
 #             cleanup_gpio()

    return counter


while True:
    start_client()
