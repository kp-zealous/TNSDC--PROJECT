import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

r = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
     machine.say(text)
     machine.runAndWait()

def get_instruction():
    try:
       with sr.Microphone(device_index=0) as source:
          print("Listening...")
          r.adjust_for_ambient_noise(source)
          speech = r.listen(source)
          instruction = r.recognize_google(speech)
          instruction = instruction.lower()
          if "jarvis" in instruction:
             instruction = instruction.replace('jarvis', "")
             print(instruction)
             return instruction
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

def play_instruction():
    instruction = get_instruction()  
    if instruction is not None and "play" in instruction:
       song = instruction.replace('play', "")
       print("Playing " , song)
       talk("Playing " + song)  
       pywhatkit.playonyt(song)
   
    elif instruction is not None and 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')  
        print('The current time is ' , time)
        talk('The current time is ' + time)
        
   
    elif instruction is not None and 'date' in instruction:
        time=datetime.datetime.now().strftime ('%d / %m / %Y')
        print("Today's date" , time)
        talk("Today's date" + time)
        
    elif instruction is not None and 'how are you' in instruction:
        
        print("I am doing great!, how about you ?")
        talk("I am doing great!, how about you ?")
        
   
    elif instruction is not None and ' what is your name' in instruction:
        print('I am Jarvis, what can I do for you?')
        talk('I am Jarvis, what can I do for you?')
        
       
    elif instruction is not None and 'who is' in instruction:
        human = instruction.replace('who is','')
        info=wikipedia.summary(human, 1)
        print(info)
        talk(info)
        
    elif instruction is not None and 'bye' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')        
        talk('Bye!see you') 
        return
       
    else:
        print('Please repeat')
       
play_instruction()

