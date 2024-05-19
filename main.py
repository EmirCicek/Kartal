import functions
counter = 0
zaman_asimi_aktif = True


functions.make_main_settings()

while True:
    try:
        trigger_command = str(functions.speech_to_text())
        if 'kartal' in trigger_command.lower() or 'hey kartal' in trigger_command.lower(): 
            print('Input :',trigger_command)
            # functions.text_to_speech('Sizi Dinliyorum')
            # playsound("Crystal.mp3")

            for i in range(3):
                trigger_command = ""
                try:
                    command = str(functions.speech_to_text("Crystal.mp3"))
                    if 'hava durumu' in command.lower() or 'hava durumunu aç' in command.lower():
                        functions.open_weather_website()
                        functions.text_to_speech('Hava Durumu Açıldı')
                        counter = 0
                        zaman_asimi_aktif = True
                        break
                    elif 'ana ekran' in command.lower() or 'ana sayfa' in command.lower():
                        functions.open_kartal()
                        functions.refresh()
                        functions.text_to_speech('Ana Ekran Açıldı')
                        counter = 0
                        zaman_asimi_aktif = True
                        break
                    elif 'saat' in command.lower():
                        functions.open_time()
                        functions.text_to_speech('Saat '+ functions.time()[0])
                        counter = 0
                        zaman_asimi_aktif = False
                        break
                    elif 'tam ekran' in command.lower() or 'ekran modu' in command.lower() or 'tam ekranı kapat'.lower() in command.lower() or 'ekranı kapat'.lower() in command.lower() or "tam ekran'ı kapat".lower() in command.lower() or "ekran'ı kapat".lower() in command.lower() or 'tam ekranı aç'.lower() in command.lower() or 'ekranı aç'.lower() in command.lower() or "tam ekran'ı aç".lower() in command.lower() or "ekran'ı aç".lower() in command.lower():
                        functions.full_screen()
                        counter = 0
                        zaman_asimi_aktif = True
                        break
                    elif 'taş' in command.lower() or 'kagit' in command.lower() or 'makas' in command.lower() or 'tas' in command.lower() or 'kagıt' in command.lower() or 'makas' in command.lower() or 'kagit' in command.lower() or 'taş kağıt makas' in command.lower() or 'tas kagıt makas' in command.lower() or 'taş kağıt makas oyununu aç' in command.lower() or 'kağıt' in command.lower():
                        functions.tas_kagit_makas()
                        functions.text_to_speech('Oyun Açıldı')
                        counter = 0
                        zaman_asimi_aktif = False
                        break
                    # elif 'ışığı aç' in command.lower() or 'lambayı aç' in command.lower():
                    #     functions.led_yak()
                    #     functions.text_to_speech('Lamba Açıldı')
                    #     counter = 0
                    #     zaman_asimi_aktif = False
                    #     break
                    # elif 'ışığı kapat' in command.lower() or 'lambayı kapat' in command.lower():
                    #     functions.led_sondur()
                    #     functions.text_to_speech('Lamba Kapatıldı')
                    #     counter = 0
                    #     zaman_asimi_aktif = False
                    #     break
                    elif 'ışığı aç' in command.lower() or 'lambayı aç' in command.lower() or "ışığı yak" in command.lower() or 'lambayı yak' in command.lower():
                        functions.open_kartal()
                        functions.led_ac()
                        functions.text_to_speech('Lamba Açıldı')
                        counter = 0
                        zaman_asimi_aktif = False
                        break
                    elif 'ışığı kapat' in command.lower() or 'lambayı kapat' in command.lower() or "ışığı söndür" in command.lower() or 'lambayı söndür' in command.lower():
                        functions.open_kartal()
                        functions.led_kapat()
                        functions.text_to_speech('Lamba Kapatıldı')
                        counter = 0
                        zaman_asimi_aktif = False
                        break
                    elif 'programımı aç' in command.lower() or 'günlük programı aç' in command.lower() or 'program' in command.lower():
                        functions.program_ayarla()
                        functions.text_to_speech('Program Açıldı')
                        counter = 0
                        zaman_asimi_aktif = False
                        break
                    else:
                        print(command)
                except Exception as error:
                    print('Komut Almaya Çalışılırken Bir Hata Oluştu')
                    print('Error',error)
                    print(command)
        else:
            trigger_command = ""
            print("Bekleniyor...")
            if zaman_asimi_aktif:
                counter += 1
                print("Sayaç : ",counter)
                if counter == 10:
                    functions.open_kartal()
                    counter = 0
            

    except Exception as error:
        print('Bir Hata Oluştu')
        print('Error',error)
