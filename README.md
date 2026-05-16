# Nova Modular AI Assistant

This folder contains a clean modular Python assistant that listens to the microphone, sends speech to OpenAI, detects emotions, and speaks replies aloud.

## Files

- `main.py` - program entry and continuous assistant loop
- `brain.py` - OpenAI client logic
- `speech_to_text.py` - microphone speech recognition
- `text_to_speech.py` - text-to-speech output
- `emotions.py` - simple emotion detection
- `commands.py` - basic exit command handling
- `web_app.py` - browser-based assistant interface
- `templates/index.html` - web chat UI
- `.env.example` - environment variable example

## Setup

1. Install dependencies:

```powershell
cd backend
python -m pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your OpenAI API key:

```powershell
copy .env.example .env
```

3. Run the assistant from the terminal:

```powershell
python main.py
```

Optionally run the browser interface:

```powershell
python web_app.py
```

Then open `http://127.0.0.1:8000` in your browser.

Say `exit` in the browser input to end the session.
