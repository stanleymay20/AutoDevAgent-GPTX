from flask import Blueprint, jsonify
from utils.auto_fix_engine import AutoFixEngine

autofix_bp = Blueprint('autofix', __name__)

@autofix_bp.route('/autofix/run')
def trigger_autofix():
    engine = AutoFixEngine()
    engine.run()
    return jsonify({"status": "AutoFix completed."})
