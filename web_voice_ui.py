from flask import Flask, request, render_template, jsonify
import whisper
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
TASK_FILE = "context/current_task.txt"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
model = whisper.load_model("base")

@app.route("/")
def index():
    return render_template("mic_ui.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["audio"]
    path = os.path.join(UPLOAD_FOLDER, "voice_input.wav")
    file.save(path)
    result = model.transcribe(path)
    task = result["text"]
    with open(TASK_FILE, "w") as f:
        f.write(task)
    return jsonify({"task": task})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

