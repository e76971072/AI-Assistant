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
                GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
        "type": "service_account",
        "project_id": "speechtotext-237520",
        "private_key_id": "a43ec6127fb553fe950fed0097b69a33a50e5317",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDlWMb+1Xw9xvL+\n41XUnfdxxtbVuCWlhCHanj7t++y49AaMyBAEBF7sUiWcvZaoGrK8RIsHwu1r+d1k\nH6Og1a3DYV4FAjt0nEx95ohzjMBTQMTRhlN6iHHQDDncuObZNJSlquEwAj8PVbmP\n95gJy7F3IbdkHKLjDtM+7Y9zrPTBgbbmkyWL9fQkGBDHId7mHDlfq+KhKNKM6AYd\nc5cb0t/GcW6FpEagMABuPgWwTYMLENeKznmsm71GpxjJ/rNEyf7Zk3rNC8Yj+AmI\ny9YpHbU9YFHUdoETLnwPumnXFJznLsqyIs/qwbuz5/2ebcT1DGI0gxk3RIv/1LZy\n4l5KpYc3AgMBAAECggEAH9wFSME/URWiC+ZotfB7v0Jv9aBvGl8QlN4Gv+iPKeI8\nRrJEB0rUJOAEeZGcrB2JVr3u0lUxxh4fsxjyEhWc3ddYyDlXKQvNVHAB5ItY7DfD\nH5gZYJwzs0L/hrno16OGQr1KKvEk8WxnKqiqZjH1pSb54t5XglM85TD7DIaqOXcY\nLCTZpoHjApS0MCx1PUDnpSW+ICED1HNlFV6az4vmoXvXtou60yjMWdpL6jyoI017\nwKut39j7fnenDW9zv24MIY+KmiBWnwlAo5mHJ9j0Doz6mpezhwHNDDTQFPMl2AvO\nBu6D3JHMQulsNRqcFYC2TT4EtWTLlIuhH4xU6VTOAQKBgQD27CjEfb54eaZAGwjN\ncMz7pWV//7oBU53Y/I3mCbMTDoLffzpV0oC1jYhsQO4tDtFZBCm/8OzPBs81RlXa\nmxOlnpd8jq4RnQKutvztzbLe7/BlTbWJevw1dKTEQzqx9c4R+uO5X7mF64E7PdmB\ncvx7DktoE8Vcb9QmQk5lT1E4BwKBgQDtxzWTk4QmgbxPaQr3/XXLusxd92Podyyp\n9Sbsgt0J+uYzoC/dCd7/N84uratN41hEFts0r1fHWPMtm1JuELETDh1lAGuhpgGC\n80QIQx53nCSH+6qGQMN7wF/8lgKOZWimMUUVVOIrTWpiIzMMnZjLT/AZ30r39e31\nGw3F+4GLUQKBgQDwR7MMMkjNN6O+MhCIykHOh46T1igM7m9mHa1/suSdoLtd/ZKo\nvSUehtHAdhbPpeG2O8Tc0PfAJiIw93bIOawOuJs1TCq7XQylM9BBIK/1HYvTKKGF\nXTZcVluX2MwfLNEQ0hIT68C/PwMMwQ0NWPW0UZ6zcrnVT8UkTdW35E1mtQKBgA0Z\n69bMyvxAK7sIY6VUXtgx267Vwbh+UISw0Es5zqoNG//+NITuVU4kqgSiZwzsmOFv\njPZzLtf6C7QYmcsculT9cxsskcGfXvfzJW17HUOj49NmR3gMO3knGWLWdR+ZcNGv\nZ0oMmkWeh10O6XIpgNC6/9S9G+lbsJfPvMuK1xFxAoGALQ/6Og5MfkdtqU/4SwhH\nxnkePA+HtS1qVDfQvken0C5MZyZqdTtr3lmDalaV6XCMUlucnG/s0NbbbrONN8xc\nYq46UPzvRY7ohI8BRZvlqmnCT4pYWetJt5IKM1GPOCef2hp2tSzshmcT6bWRjXRD\nqkwvEIZuJP2BRZPvRcP4Nfc=\n-----END PRIVATE KEY-----\n",
        "client_email": "starting-account-fx8bhbxzwe5t@speechtotext-237520.iam.gserviceaccount.com",
        "client_id": "117562214576723795773",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-fx8bhbxzwe5t%40speechtotext-237520.iam.gserviceaccount.com"
        }
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
        account_sid = 'AC4380ca008e9d36cfc7d279d81425e6f4'
        auth_token = '88b88e0041b54c2e35cf370800417082'
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
        account_sid = 'AC4380ca008e9d36cfc7d279d81425e6f4'
        auth_token = '88b88e0041b54c2e35cf370800417082'
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
