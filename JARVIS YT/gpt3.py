import nltk
from nltk.stem import LancasterStemmer
import numpy as np
import pickle
import random
import json
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time
import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
import openai
# import chatopenai
 
openai.api_key=os.getenv("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")
 
def chat_gpt3(zice):
    response = openai.Completion.create(
        engine="davinci",
        # prompt=zice,
        prompt=" Human: "+zice+"\nAI",
        temperature=0.1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    print(response)
    return response.choices[0].text.split(": ")[1]
 
r = sr.Recognizer()
session = Session(profile_name="default")
transcribe_client  = session.client('transcribe')
polly=session.client("polly")
 
def aws_tts(text):
    response = polly.synthesize_speech(VoiceId='Kevin',
                OutputFormat='mp3', 
                Text = text,
                Engine = 'neural')
    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
 
while (True) :
    hopa=input('Enter to continue')
    with sr.Microphone(device_index=2) as mic:
            print("speak, human!")
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic, phrase_time_limit=6)
            with open("input.wav",'wb') as f:
                f.write(audio.get_wav_data())
            try:
                inp = r.recognize_google(audio)
                print(inp)
                inp = inp.lower()
                raspuns= chat_gpt3(inp)
                aws_tts(raspuns)
                os.startfile("speech.mp3")
                os.remove("speech.mp3")
            except Exception as e:
                print("Could not understand", e)