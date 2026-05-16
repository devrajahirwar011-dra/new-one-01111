import speech_recognition as sr


class SpeechRecognizer:
    """Handles listening to microphone audio and converting it to text."""

    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self) -> str:
        """Listen to the microphone and return the recognized text."""
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)

        try:
            text = self.recognizer.recognize_google(audio)
            return text.strip()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please try again.")
            return ""
        except sr.RequestError as error:
            print(f"Speech recognition error: {error}")
            return ""
