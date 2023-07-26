import speech_recognition as sr
import text_to_speech as ts
def myspeechrecognition(duration):# Initialize the recognizer
    r = sr.Recognizer()
    # Set the microphone as the audio source
    mic = sr.Microphone()
    # Adjust for ambient noise levels
    with mic as source:
        r.adjust_for_ambient_noise(source)
    # Set the recording duration (in seconds)
    recording_duration = duration
    # Start recording
    ts.say("Listening....")
    with mic as source:
        audio = r.record(source, duration=recording_duration)
    # Perform speech recognition
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        ts.say("Sorry, I could not understand what you said , Please try to speak again")
        text = myspeechrecognition(duration)
        print(text)
    except sr.RequestError as e:
            ts.say("Could not request results from the Speech Recognition service; {0}".format(e))
    finally:
        return text.lower()
