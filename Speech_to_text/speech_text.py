#!/usr/bin/env python



def run_quickstart():
    # [START speech_quickstart]
    import io
    import os
    import time

    # Imports the Google Cloud client library
    # [START speech_python_migration_imports]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # [END speech_python_migration_imports]

    # Instantiates a clients
    # [START speech_python_migration_client]
    client = speech.SpeechClient()
    # [END speech_python_migration_client]

    # The name of the audio file to transcribe

    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'motivation.flac')
    # Loads the audio into memory
    #file_name = 'Obama.mp3'
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        #sample_rate_hertz=16000,
        language_code='en-US')
    print (time.time())
    print (f"{time.ctime()} Before")
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    print (f"{time.ctime()} After")
    print(response)
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    # [END speech_quickstart]
if __name__ == '__main__':
    run_quickstart()