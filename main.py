import os

if __name__ == '__main__':
    print("Welcome to RoboSpeak 1.1. Created by Ahsan Tariq")
    while True:
        x = input("Enter what you want me to speak or type q to quit': ")
        if x == "q":
            os.system(f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Exiting... Bye bye buddy, see you soon.');" ''')
            break
        command = f''' PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');" '''
        os.system(command)