from dotenv import load_dotenv

from brain import OpenAIBrain
from emotions import EmotionDetector
from text_to_speech import TextSpeaker

# Load environment variables from the .env file.
load_dotenv()


def main() -> None:
    """Run the assistant from the terminal until the user types exit."""
    speaker = TextSpeaker()
    brain = OpenAIBrain()
    emotion_detector = EmotionDetector()

    print("Nova AI assistant is ready. Type a message or 'exit' to quit.")
    speaker.speak("Nova is ready. Type a message to begin.")

    while True:
        user_text = input("You: ").strip()
        if not user_text:
            continue

        if user_text.lower() == "exit":
            farewell = "Goodbye. See you again soon."
            print(f"AI: {farewell}")
            speaker.speak(farewell)
            break

        ai_response = brain.generate_response(user_text)
        emotion = emotion_detector.detect_emotion(ai_response)

        print(f"AI: {ai_response}")
        print(f"Emotion: {emotion}")

        speaker.speak(ai_response)


if __name__ == "__main__":
    main()
