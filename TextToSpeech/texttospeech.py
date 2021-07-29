# install ibm watson first by write  (pip install ibm_watson)


# install 
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'knB5dQTayVT5Fk3Jybh_JywnlA0ctl8PpcKlxic0h5aE'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/dd7e7bd1-e274-478c-af3b-769c2378237b'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


# open the file to read the text
with open('outputss.txt', 'r') as f:
    text = f.readlines()

    
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)


# create a mp3 to save the speech 
with open('./testspeech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)