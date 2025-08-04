from win32com.client import Dispatch

if __name__ == '__main__':
    speaker = Dispatch("SAPI.SpVoice")
    print("Welcome to RoboSpeaker for Windows. Created by Kashaf")

    while True:
        x = input('Enter what you want me to speak: ')
        if x.lower() == 'q':
           speaker.Speak('Bye bye Friend!')
           break

        speaker.Speak(x)




