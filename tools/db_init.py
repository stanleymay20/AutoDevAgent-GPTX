from app import db
from flask import Flask

# Setup context if needed
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()
    print("✅ Database initialized.")
