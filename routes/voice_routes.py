from flask import Blueprint, render_template, request, jsonify
from voice.whisper_transcriber import transcribe_audio
from agents.sea_agent import respond_to_voice

voice_bp = Blueprint('voice', __name__)

@voice_bp.route('/')
def voice_console():
    return render_template('voice.html')

@voice_bp.route('/whisper', methods=['POST'])
def whisper():
    audio_file = request.files['audio']
    transcript = transcribe_audio(audio_file)
    ai_response = respond_to_voice(transcript)
    return jsonify({"transcript": transcript, "response": ai_response})
