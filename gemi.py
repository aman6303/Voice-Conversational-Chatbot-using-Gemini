import speech_recognition as sr
from google.generativeai import GenerativeModel
import google.generativeai as genai
from gtts import gTTS
import os
# import pyglet
# import pyaudio
import pygame, time
pygame.init()

API_KEY = "AIzaSyCj_t8vfIkwI3pq2ILf6FCbAPXpB6qddFU"


genai.configure(api_key=API_KEY)
generation_config={
    "temperature":0.7,
    "top_p":1,
    "top_k":1,
    "max_output_tokens":2048
}
model = GenerativeModel("gemini-pro", generation_config=generation_config)


def recognize_speech():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak your question:")
    audio = r.listen(source)
  try:
    user_input = r.recognize_google(audio)
    print("You said: " + user_input)
    return user_input
  except sr.UnknownValueError:
    print("Sorry could not understand audio")
    return None

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")


    pygame.mixer.music.load('response.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    # pygame.mixer.music.fadeout(5)
    pygame.mixer.music.unload()

    

while True:
  user_question = recognize_speech()
  if user_question is not None:
    response = model.generate_content(user_question)
    print(f"Gemini: {response.text}")
    speak(response.text) 
