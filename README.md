# IBM-Text-To-Speech

# The task about how to convert a text file to speech and store the speech as mp3  

* I work with IBM cloud and select the service ( Text To Speech )

* setup the apikey and url inside texttospeech.py 

* install the requierment   by type    ( pip install ibm_watson )

* run the python code texttospeech.py   by write   ( python texttospeech.py  ) 





### After that to save the speech in as mp3 :

so to do this I add the code below to **texttospeech.py page**

with open('./testspeech.mp3', 'wb') as audio_file:
res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
audio_file.write(res.content)



 
**The outputss.txt :** file contains the text 
 
**The testspeech.mp3 :** audio file 
