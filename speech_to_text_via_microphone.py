# NOTE: this example requires SpeechRecognition because it uses the recognizer class (pip install SpeechRecognition)
# NOTE: this example requires PyAudio because it uses the Microphone class (pip install PyAudio)

#import library

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")
