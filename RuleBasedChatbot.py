import datetime
import time
import pyttsx3

engine=pyttsx3.init()

def speak(input):
    engine.say(input)
    engine.runAndWait()
    
present_time=datetime.datetime.now().hour

name= input("Enter your name :")
if 5 <= present_time < 12:
    speak(f"Good Morning {name}",)
    print(f"Good Morning {name}",)

elif 12 <= present_time < 17:
    speak(f"Good Afternoon  {name}")
    print(f"Good Afternoon  {name}")

elif 17 <= present_time < 21:
    speak(f"Good Evening {name}")
    print(f"Good Evening {name}")

else:
    speak(f"Good Night {name}")
    print(f"Good Night {name}")





print("Hello! To Your Chatbot")
speak("Hello! To Your Chatbot")

print("You can ask me a basic question , Type 'bye' to exit")
speak("You can ask me a basic question , Type 'bye' to exit")

response={
    'hello':"Hi,welcome. How can I help you?",
    'how are u':"I am fine what about u",
    'who are u':'I am Ai chat bot',
    'motivate me': 'Take a look toward your parents',
    'what is function':'small block of code ..That we use every time when we call it'
    
}



#fucntion
def getResponseofBot(userQuestion):
    
    for i in response:
        if i==userQuestion:
            return  response[i]
     
    return "I am not able to tell that yet" 
     
     
while True:
    userInput=input("Please ask your questionn:")
    userInput=userInput.lower()
    
    if userInput=='bye':
        print('See u soon bro....')
        speak('See u soon bro....')
        break
    
    reply=getResponseofBot(userInput)
    print("Bot Response : ",reply)
    speak(f"Bot Response : {reply}")
