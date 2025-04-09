#!/bin/bash

echo "🚀 Deploying AutoDevAgent-GPTX project..."

# Example: using Python + Flask for now
echo "Starting Flask App..."
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
