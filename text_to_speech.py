import pyttsx3


class TextSpeaker:
    """Speaks text aloud using pyttsx3."""

    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)
        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text: str) -> None:
        """Convert text to speech and play the spoken audio."""
        if not text:
            return
        self.engine.say(text)
        self.engine.runAndWait()
