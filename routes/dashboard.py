from flask import Blueprint, request, jsonify, render_template
from core.executor import execute_task
from agents.gpt_injector import run_command

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboard_bp.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    task = data.get("task", "")
    result = execute_task(task)
    return jsonify({"response": result})

@dashboard_bp.route('/run', methods=['POST'])
def run_directive():
    data = request.get_json()
    cmd = data.get("command", "")
    output = run_command(cmd)
    return jsonify({"result": output})
