from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

from brain import OpenAIBrain
from emotions import EmotionDetector
from text_to_speech import TextSpeaker

# Load environment variables so OpenAI keys work.
load_dotenv()

app = Flask(__name__, template_folder="templates")
brain = OpenAIBrain()
emotion_detector = EmotionDetector()
speaker = TextSpeaker()

conversation_history = []


@app.route("/")
def home() -> str:
    """Render the web chat interface."""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat() -> tuple[dict, int]:
    """Receive a message from the browser and return the AI response."""
    data = request.get_json(force=True)
    user_text = data.get("message", "").strip()

    if not user_text:
        return {"error": "Please type a message."}, 400

    if user_text.lower() == "exit":
        farewell = "Goodbye. Refresh the page to start again."
        speaker.speak(farewell)
        return {
            "response": farewell,
            "emotion": "neutral",
            "ended": True,
        }, 200

    conversation_history.append({"role": "user", "content": user_text})
    ai_response = brain.generate_response(user_text)
    conversation_history.append({"role": "assistant", "content": ai_response})

    emotion = emotion_detector.detect_emotion(ai_response)
    speaker.speak(ai_response)

    return {
        "response": ai_response,
        "emotion": emotion,
        "ended": False,
    }, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
