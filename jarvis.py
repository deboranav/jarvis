import pyttsx3 #pip install pyttsx3
import datetime 
import speech_recognition as sr #Reconhecimento de voz agora se chama sr

engine = pyttsx3.init()

def speak(audio): #Função de aúdio usando a biblioteca pyttsx3
   
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak ("Agora são: ")
    speak (Time)


def date_() :
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak ("Hoje é: ")
    speak (date)
    speak ("do")
    speak (month)
    speak ("de")
    speak (year)
    
def wishme() :
    speak ("Bem vinda de volta, Débora")
    date_()
    time()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12:
        speak("Bom dia, parcêra")
    elif hour >=12 and hour <18:
        speak("Boa tarde, parcêra")
    elif hour >=18 and hour <24:
        speak("Boa noite, parcêra")
    else:
        speak("Tá fazendo o que acordada, mulhé?")

    speak("Jarvis a seu serviço, o que posso fazer por você hoje?")

def TakeComand():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer() 
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        speak("Tô te ouvindo...")
        microfone.pause_threshold= 1
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        speak ("reconhecendo...")
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        Frase = microfone.recognize_google(audio, language = 'pt-BR')
        #Após alguns segundos, retorna a frase falada
        print("Você disse: " + Frase)

    except Exception as e:
        print(e)
        print("Pode repetir, por favor")
        return "None"
    return Frase

if __name__ == "__main__":

    wishme()

    while True:
        Frase = TakeComand().lower()

        #all comands will be store in lower case in frase
        #for easy recognition 

        if 'hora' in Frase: #tell us time when asked
            time()

        if 'data' in Frase:
            date_()

        if 'obrigada' in Frase:
            speak("De nada, estou as ordens")
            break







