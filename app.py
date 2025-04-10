from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from routes.index import index_bp
from routes.dashboard import dashboard_bp
from routes.voice_routes import voice_bp
import whisper
import os
from routes.watchdog import watchdog_bp
from routes.autofix import autofix_bp

# === Flask App Init ===
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# === Database Model ===
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# === Blueprint Routes ===
app.register_blueprint(index_bp)
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(voice_bp, url_prefix='/voice')
app.register_blueprint(watchdog_bp, url_prefix='/watchdog')
app.register_blueprint(autofix_bp, url_prefix='/autofix')

# === Local Routes for DB Task Handling ===
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        db.session.add(Task(title=title))
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task = db.session.get(Task, id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    task = db.session.get(Task, id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    upload_path = "uploads"
    os.makedirs(upload_path, exist_ok=True)
    path = os.path.join(upload_path, "audio.webm")
    file.save(path)

    model = whisper.load_model("base")
    result = model.transcribe(path)
    task_text = result['text'].strip()

    if task_text:
        db.session.add(Task(title=task_text))
        db.session.commit()

    return redirect(url_for('index'))

# === Run App ===
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5050)
