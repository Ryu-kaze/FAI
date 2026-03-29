import speech_recognition as sr
import pyttsx3

def speech_to_text(recognizer):
    try:
        with sr.Microphone() as source:
            print("Speak now...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("Recognized Text:", text)

        except sr.UnknownValueError:
            print("Speech not recognized. Please try again.")

        except sr.RequestError:
            print("Could not connect to recognition service.")

    except Exception as e:
        print("Microphone Error:", e)


def text_to_speech(engine):
    try:
        text = input("Enter text to convert into speech: ").strip()

        if not text:
            raise ValueError("Text cannot be empty.")

        engine.say(text)
        engine.runAndWait()

        print("Text has been converted to speech.")

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("System Error:", e)


# --------- Main Program ---------
engine = pyttsx3.init()
recognizer = sr.Recognizer()

while True:
    try:
        choice = input("Enter 1 for Speech-to-Text, 2 for Text-to-Speech: ").strip()

        if choice == "1":
            speech_to_text(recognizer)
            break

        elif choice == "2":
            text_to_speech(engine)
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except Exception as e:
        print("Unexpected Error:", e)
