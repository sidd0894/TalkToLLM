import pyttsx3 as tts
import speech_recognition as sr


class SpeechToSpeech:
    @staticmethod
    def speech_to_text():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                # print("You said:", text)
                return text
                # self.__get_response(user_prompt=text)
            except sr.UnknownValueError:
                raise ValueError("[ERROR] Could not understand audio")
            except sr.RequestError:
                raise ConnectionError("[ERROR] Could not request results from Google API")

    @staticmethod
    def text_to_speech(text, speech_rate=150, voice_index=0):
        engine = tts.init()
        engine.setProperty('rate', speech_rate)
        # engine.setProperty('volume', 0.9)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_index].id)
        engine.say(text)
        engine.runAndWait()


