from datetime import datetime
import speech_recognition  # распознавание речи 
import pyttsx3  # синтез речи
import webbrowser  # открывание вкладок 
import traceback 
import wave  
import os  
class VoiceAssistant: # в потенциале для возможности нескольких ассистенток
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    voices = ttsEngine.getProperty("voices")
    assistant.recognition_language = "ru-RU"



def record_and_recognize_audio(*args: tuple):# запись
    with microphone:
        recognized_data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Я слушаю")
            audio = recognizer.listen(microphone, 5, 5)

            with open("audio.wav", "wb")  as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            assistant_speech(translator.get("Проверь микрофон"))
            traceback.print_exc()
            return
        try:
            recognized_data = recognizer.recognize_google(audio, language=assistant.recognition_language).lower()

        except speech_recognition.UnknownValueError:
            pass 

        return recognized_data

def assistant_speech(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()
    
def time(*args: tuple):
    current_datetime = datetime.now()
    assistant_speech(str(current_datetime.hour) + "часов"+str(current_datetime.minute)+"минут")
        

def thanks(*args: tuple):#блок благодарств
    if command == "спасибо":
         assistant_speech("Рада помочь!")
    if command == "благодарю":
         assistant_speech("Какие манеры! обращайтесь")

         
def greeting(*args: tuple):#блок приветствия

    if command == "добрый день":
         assistant_speech("добрый день!")
    if command == "добрый вечер":
         assistant_speech("хороший вечерок")
    if command == "доброе утро":
         assistant_speech("доброе утро!")
    if command == "здравствуй":
         assistant_speech("здравствуй!")
    if command == "привет":
         assistant_speech("привет!")
    

def farewell(*args: tuple):# блок прощания

    if command == "хорошего дня":
         assistant_speech("И тебе хорошего дня!")
         ttsEngine.stop()
    if command == "спокойной ночи":
         assistant_speech("Хороших снов!")
         ttsEngine.stop()
    if command == "до свидания":
         assistant_speech("буду рада увидиться снова!")
         ttsEngine.stop()
    if command == "пока":
         assistant_speech("Пока!")
         ttsEngine.stop()
    quit()

def weather_forecast (*args: tuple):# блок погоды
     url = "https://yandex.ru/pogoda/?lat=60.000061&lon=30.252703&utm_content=main_informer&utm_source=home&utm_medium=web&utm_campaign=informer&utm_term=title"
     webbrowser.get().open(url)
     assistant_speech("Я открыла!")
     
def acquaintance ():#блок знакомства
     assistant_speech("Я -Лайя. Я - голосовая помошница. Могу открыть ютуб, яндекс музыку и прогноз погоды, так же подскажу какое сейчас время")

def youtube(*args: tuple):#блок открытия ютуба 
    url = "https://www.youtube.com"
    webbrowser.get().open(url)
    assistant_speech("Я открыла!")

def play_music (*args: tuple):# открытие яндекс музыки
   
    url = "https://music.yandex.ru/home" 
    webbrowser.get().open(url)
    assistant_speech("Я открыла!")

def do_command(command_name: str, *args: list):
    for   key in commands.keys() :
        if   command_name in key:
            commands[key](*args)
        else:
            pass  
          
commands = {#список команд
 ("добрый день", "добрый вечер", "доброе утро", "привет","здравствуй"): greeting,
 ( "до свидания", "спокойной ночи", "пока", "хорошего дня"): farewell,
 ( "открой youtube", "youtube", "видео"): youtube,
 ( "сколько времени", "какое сейчас время", "время"): time,
 ( "открой яндекс музыку", "яндекс музыка", "музыка"): play_music,
  ( "кто ты", "что ты можешь"): acquaintance,
  ( "прогноз погоды", "погода"): weather_forecast,
 ( "спасибо", "блогодарю"):thanks,

}

if __name__ == "__main__":
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    ttsEngine = pyttsx3.init()
    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Лайя"
    assistant.sex = "female"
    assistant.speech_language = "ru"
    setup_assistant_voice()
    while True:
        voice_input = record_and_recognize_audio()
        print(voice_input)
        os.remove("audio.wav")
        command = voice_input
        do_command(voice_input)
