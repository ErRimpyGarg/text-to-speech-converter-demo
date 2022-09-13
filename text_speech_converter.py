import pyttsx3

speaker = pyttsx3.init()

list_of_voices = speaker.getProperty('voices')

speaker.setProperty('voice', list_of_voices[1].id)
speaker.say("Hi, How are you?. I am doing wonderful. Thank you.")
speaker.runAndWait()