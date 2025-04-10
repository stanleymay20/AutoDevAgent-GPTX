from flask import Blueprint, render_template, jsonify
import json
import os

watchdog_bp = Blueprint('watchdog', __name__)

# Route: HTML dashboard with preloaded suggestions
@watchdog_bp.route('/watchdog')
def watchdog_dashboard():
    suggestion_log_path = "logs/suggestions.json"
    suggestions = []
    if os.path.exists(suggestion_log_path):
        with open(suggestion_log_path, 'r') as f:
            suggestions = json.load(f)
    return render_template("watchdog_dashboard.html", suggestions=suggestions)

# Route: JSON API for dynamic frontend refresh (AJAX support)
@watchdog_bp.route('/watchdog/data')
def watchdog_data():
    suggestion_log_path = "logs/suggestions.json"
    suggestions = []
    if os.path.exists(suggestion_log_path):
        with open(suggestion_log_path, 'r') as f:
            suggestions = json.load(f)
    return jsonify(suggestions)
