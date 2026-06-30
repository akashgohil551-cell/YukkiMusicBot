from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

