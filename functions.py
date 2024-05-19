import pyautogui
from responsive_voice import ResponsiveVoice
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS 
import os 
from playsound import playsound
from time import sleep
import socket
import serial


# try:
#     import RPi.GPIO as GPIO
# except ModuleNotFoundError:
#     print("Raspberry Pi modülü bulunamadı. Lütfen 'sudo apt-get install python3-rpi.gpio' komutunu çalıştırın.")


def make_main_settings():
    os.startfile("index.html")
    sleep(2)
    open_kartal()
    full_screen()

# def led_yak(pin=11):
#     try:
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.setup(pin, GPIO.OUT)
#         GPIO.output(pin, GPIO.HIGH)
#     except:
#         print("Modülü indirmeyi deneyin ve bu özellik için linux kullanın --> 'sudo apt-get install python3-rpi.gpio'   --> led_yak()")

# def led_sondur(pin=11):
#     try:
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.setup(pin, GPIO.OUT)
#         GPIO.output(pin, GPIO.LOW)
#     except:
#         print("Modülü indirmeyi deneyin ve bu özellik için linux kullanın --> 'sudo apt-get install python3-rpi.gpio' --> led_sondur()")

def speech_to_text(audio=None): 
    recognizer = sr.Recognizer() 
 
    try: 
        # Mikrofondan sesi dinle 
        with sr.Microphone() as source: 
            print("Dinleniyor...")
            recognizer.adjust_for_ambient_noise(source)
            if audio:
                playsound(audio)
            ses = recognizer.listen(source, timeout=1.5) 
        metin = recognizer.recognize_google(ses, language="tr-TR") 
        return metin 
    except sr.RequestError as e: 
        print("Google Web Speech API kullanılamıyor; {0}".format(e))
        return None 
    except sr.UnknownValueError: 
        print("Ses anlaşılamadı.")
        return None 
    except sr.WaitTimeoutError: 
        print("Ses alma zaman aşımına uğradı.") 
    return None

def text_to_speech(veri): 
    if veri != None: 
        tts = gTTS(text=veri, lang='tr') 
        tts.save("sesli_okuma.mp3") 
        print("Response:", veri) 
        playsound("sesli_okuma.mp3") 
        os.remove("sesli_okuma.mp3")


def clear_file(file, input): # This function clears the javascript file
    with open(file, 'w', encoding='utf-8') as fl:
        fl.write(input)

def update_file(r_file, w_file, start, finish): # This function updates the file
    with open(r_file, 'r+', encoding='utf-8') as fl:
        source_code = fl.readlines()
        clear_file(w_file, '\n')

        with open(w_file, 'a', encoding='utf-8') as file:
            started = False

            for line in source_code:
                if start == line.strip():
                    started = True
                    continue
                elif finish in line and started == True:
                    break
                elif started == True:
                    file.write(line)

def refresh():
    pyautogui.leftClick(50,300) # Clicking the browser for refresh
    pyautogui.hotkey('ctrl','f5') # Refreshing the browser

def full_screen():
    pyautogui.leftClick(50,300)
    pyautogui.hotkey('f11')

def open_weather_website():
    update_file('source.txt','script.js','hava-durumu-js-start','hava-durumu-js-end')
    update_file('source.txt','index.html','hava-durumu-html-start','hava-durumu-html-end')
    refresh()

DAYS = {
    'Monday' : 'Pazartesi',
    'Tuesday' : 'Salı',
    'Wednesday' : 'Çarşamba',
    'Thursday' : 'Perşembe',
    'Friday' : 'Cuma',
    'Saturday' : 'Cumartesi',
    'Sunday' : 'Pazar'
}


def time_t():

    
    now = datetime.now()
    hour = now.strftime("%H:%M")
    # date = now.strftime("%Y-%m-%d")
    date = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")

    result = [hour,date,DAYS[day]]

    return result # [0] --> 12:38 [1] --> 25-11-2023 [2] --> Saturday(Cumartesi)


def open_time():
    update_file('source.txt','index.html','saat-html-start','saat-html-end')
    update_file('source.txt','script.js','saat-js-start','saat-js-end')
    refresh()

def tas_kagit_makas():
    update_file('source.txt','index.html','game-html-start','game-html-end')
    update_file('source.txt','script.js','game-js-start','game-js-end')
    refresh()

def open_kartal():
    update_file("source.txt","index.html","kartal-html-start","kartal-html-end")
    refresh()

def start_server(veri):  # 1 = lamba aç, 2 = lamba kapat
    # Server bilgileri
    host = '192.168.1.21'
    port = 12345

    print("Bilgisayar IP:", socket.gethostbyname(socket.gethostname()))
    print("Kullanılan IP:", host)

    # Server socket oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server başlatıldı ve bağlantı bekleniyor...")

    # Client bağlandığında
    conn, addr = server_socket.accept()
    print(f"Bağlantı sağlandı: {addr}")

    # Gönderilecek veri
    data = str(veri)

    # Veriyi client'a gönder
    conn.send(data.encode())

    # Bağlantıyı kapat
    conn.close()
    server_socket.close()
    print("Server kapatıldı.")


def led_ac():
    start_server(1)

def led_kapat():
    start_server(2)

# def led(kontrol): # 1 açma 2 kapatma
#     port = serial.Serial('com3', 9600)

#     if kontrol == 1:
#         port.write(b'1')

#     elif kontrol == 2:
#         port.write(b'2')


# led(1)

def read_program(): # This function reads the program.txt file for today's program
    clear_file('program-data.txt','')
    day = time_t()[2].lower()
    start = day+'-start'
    end = day+'-end'

    with open('program.txt','r', encoding='utf-8') as file:
        control = False
        lines = file.readlines()
        for line in lines:
            if start in line:
                control = True
            elif end in line:
                control = False
            elif control == True:
                with open('program-data.txt','a', encoding='utf-8') as file:
                    file.write(line)
    
def sort_program(): # This function sorts the data.txt file --> Use when you run read_program()
    with open('program-data.txt','r', encoding='utf-8') as file:
        lines = file.readlines()
        lines.sort()
        clear_file('program-data.txt',"")
        with open('program-data.txt','w', encoding='utf-8') as file:
            file.writelines(lines)

def html_line():
    with open('program-data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        clear_file('data.txt', '')
        for line in lines:
            if line != '\n':
                data_set = line.split()
                color = "white"
                activity_color_list = sorted([str(data_set[1]), str(time_t()[0])])
                if activity_color_list[0] == time_t()[0]: # renk ayarla
                    pass
                
                time = data_set[0] + ' - ' + data_set[1]
                activity = data_set[2]
                with open('data.txt', 'a', encoding='utf-8') as data_file:
                    data_file.write('<div style="background-color: '+color+';" class="row text-center"> \n')
                    data_file.write('<div style="border: 3px solid black;" class="saat-box col-4"><h3>'+time+'</h3></div> \n')
                    data_file.write('<div style="border: 3px solid black;" class="etkinlik-box col-8"><h3>'+activity+'</h3></div> \n')
                    data_file.write('</div> \n')
        
    with open('data.txt', 'r', encoding='utf-8') as file:
        # update_file('source.txt', 'index.html', 'html-line-1-start', 'etkinlik-html-end')
        clear_file('index.html', '')
        with open("source.txt", "r", encoding='utf-8') as file_1:
            lines = file_1.readlines()
            control = False
            for line in lines:
                if "html-line-1-start" in line:
                    control = True
                elif "html-line-1-end" in line:
                    control = False
                elif control == True:
                    with open('index.html', 'a', encoding='utf-8') as main_file:
                        main_file.write(line)

        lines = file.readlines()
        for line in lines:
            with open('index.html', 'a', encoding='utf-8') as main_file:
                main_file.write(line)
        # update_file('source.txt', 'index.html', 'html-line-2-start', 'html-line-2-end', clear=False)
        with open("source.txt", "r", encoding='utf-8') as file_1:
            lines = file_1.readlines()
            control = False
            for line in lines:
                if "html-line-2-start" in line:
                    control = True
                elif "html-line-2-end" in line:
                    control = False
                elif control == True:
                    with open('index.html', 'a', encoding='utf-8') as main_file:
                        main_file.write(line)



def program_ayarla():
    read_program()
    sort_program()
    html_line()
    refresh()

