import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
   print("Speak Anything : ")
   audio=r.listen(source)
   try:
     text=r.recognize_google(audio) 
     print("What you said : {}".format(text))
   except:
     print("Sorry can you repeat what you said a bit louder")
