import pyautogui
from responsive_voice import ResponsiveVoice
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS 
import os 
from playsound import playsound
from time import sleep

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("Raspberry Pi modülü bulunamadı. Lütfen 'sudo apt-get install python3-rpi.gpio' komutunu çalıştırın.")


def make_main_settings():
    os.startfile("index.html")
    sleep(2)
    open_kartal()
    full_screen()

def led_yak(pin=11):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    except:
        print("Modülü indirmeyi deneyin ve bu özellik için linux kullanın --> 'sudo apt-get install python3-rpi.gpio'   --> led_yak()")

def led_sondur(pin=11):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    except:
        print("Modülü indirmeyi deneyin ve bu özellik için linux kullanın --> 'sudo apt-get install python3-rpi.gpio' --> led_sondur()")

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


# def clear_file(file,input): # This function clears the javascript file
#     with open(file,'w' , encoding="utf-8") as fl:
#         fl.write(input)

# def update_file(r_file,w_file,start,finish): # This function updates the file
#     with open(r_file,'r+' , encoding="utf-8") as fl:
#         source_code = fl.readlines()
#         clear_file(w_file,'\n')

#         with open(w_file,'a') as file:
#             started = False

#             for line in source_code:
#                 if start == line.strip():
#                     started = True
#                     continue
#                 elif finish in line and started == True:
#                     break
#                 elif started == True:
#                     file.write(line)

def clear_file(file,input): # This function clears the javascript file
    with open(file,'w', encoding='utf-8') as fl:
        fl.write(input)

def update_file(r_file,w_file,start,finish): # This function updates the file
    with open(r_file,'r+', encoding='utf-8') as fl:
        source_code = fl.readlines()
        clear_file(w_file,'\n')

        with open(w_file,'a', encoding='utf-8') as file:
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



def time():
    days = {
        'Monday' : 'Pazartesi',
        'Tuesday' : 'Salı',
        'Wednesday' : 'Çarşamba',
        'Thursday' : 'Perşembe',
        'Friday' : 'Cuma',
        'Saturday' : 'Cumartesi',
        'Sunday' : 'Pazar'
    }
    
    now = datetime.now()
    hour = now.strftime("%H:%M")
    # date = now.strftime("%Y-%m-%d")
    date = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")

    result = [hour,date,days[day]]

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