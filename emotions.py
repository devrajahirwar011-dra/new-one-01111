class EmotionDetector:
    """Detects emotion from the AI response text."""

    def detect_emotion(self, text: str) -> str:
        """Return a simple emotion label based on keywords."""
        normalized = text.lower()
        if any(word in normalized for word in ["happy", "joy", "glad", "pleased", "delighted"]):
            return "happy"
        if any(word in normalized for word in ["sad", "sorry", "upset", "regret"]):
            return "sad"
        if any(word in normalized for word in ["angry", "frustrated", "irritated", "upset"]):
            return "angry"
        if any(word in normalized for word in ["excited", "awesome", "fantastic", "great", "amazing"]):
            return "excited"
        return "neutral"
