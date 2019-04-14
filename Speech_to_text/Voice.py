#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import sys
import facebook
from twilio.rest import Client
# obtain audio from the microphone

def main ():
        call_recignition()
        send_messages()
def call_recignition ():
        n = 1
        r = sr.Recognizer()
        while n > 0 :
                with sr.Microphone() as source:
                        print("Please Say Something!")
                        audio = r.listen(source)
        # recognize speech using Google Speech Recognition
                try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
                        print("  Google Speech Recognition thinks you said " + r.recognize_google(audio))
                        if r.recognize_google(audio).lower() == 'stop'.lower():
                                n = 0
                        with open ('phoneList.text', 'r') as infile:
                                line = infile.read().split()
                        checking_command(r.recognize_google(audio),line)
                except sr.UnknownValueError:
                        print("  Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                        print("  Could not request results from Google Speech Recognition service; {0}".format(e))

        # recognize speech using Google Cloud Speech
                GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{"My Private Json"}
        """
                try:
                        print("  Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
                except sr.UnknownValueError:
                        print("  Google Cloud Speech could not understand audio")
                except sr.RequestError as e:
                        print("  Could not request results from Google Cloud Speech service; {0}".format(e))
'''
        using Twiolio API to call
'''
def read_files_phoneNumbers (auto_text, line):
        found  = auto_text.split()
        for i in range(len(line)):
                if line[i].lower() == found[1].lower():
                        calling_client (line[i+1])
def calling_client (phoneNumber):
        account_sid = 'My sid'
        auth_token = 'my access token'
        client = Client(account_sid, auth_token)
        call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=phoneNumber,
                        from_='+15127102536'
                    )
        print(call.sid)
'''
        sending messages with Twiolio API
'''
def send_messages():
        account_sid = 'My sid'
        auth_token = 'my access token'
        client = Client(account_sid, auth_token)
        client.messages.create(to="+15125658778", 
                       from_="+15127102536", 
                       body="Whatever you want to say")
def checking_command (audio_text, line):
        print (audio_text)
        value = audio_text.split()
        if audio_text.lower() == 'messsage'.lower():
                send_messages()
        if value[0].lower() == 'call'.lower():
                read_files_phoneNumbers(audio_text,line)
        if audio_text.lower() == 'send help'.lower():
                emergency_help()
        if audio_text.lower() == 'facebook'.lower():
                facebook_posting()
def emergency_help ():
        account_sid = 'AC4380ca008e9d36cfc7d279d81425e6f4'
        auth_token = '88b88e0041b54c2e35cf370800417082'
        client = Client(account_sid, auth_token)
        call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+15125658778',
                        from_='+15127102536'
                    )
def facebook_posting ():
        access_token='EAAhtKNxSilUBAEUSkLdYBHzZCAMF2ApewTc6mggdWBoOWg4ZCquQfAz5nP17jswnxcFWtCqooR3KInYLErbZC4ulgEsZCOVqRyYI6iFzPjdKHriX5tM2VXfLrMa0eNWbv7l0WB9eLs43Ur2UgKk3BPJCL46IUbkl4XOIcUBAGY4vY1iu6fOjn8OcTr8pe9j6tNFBydDpGAZDZD'
        graph = facebook.GraphAPI(access_token)
        graph.put_object("me", "feed", message="Posting on my wall1!")
        #to get your posts/feed
        feed = graph.get_connections("me", "feed")
        post = feed["data"]
        print (post)
        #to put comments for particular post id
        graph.put_object(post["id"], "comments", message="First!")
main()
