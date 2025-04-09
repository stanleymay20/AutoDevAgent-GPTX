
![AutoDevAgent-GPTX Logo](logo.svg)

# 🧠 AutoDevAgent-GPTX

> The first open, universal GPT developer agent that builds your projects while you sleep.

**AutoDevAgent-GPTX** is an autonomous, memory-aware, real-code-generating GPT-4 agent that works inside your GitHub Codespace. It reads your project context and current task, writes real code, commits it, and keeps working — cycle after cycle.

---

## ✨ Features

✅ Autonomous GPT-4 code generation  
✅ Task & memory loop with logs  
✅ Auto GitHub commit & push  
✅ Flask/React starter templates  
✅ Utility tools: clone, deploy, DB init  
✅ Modular and extensible  
✅ Works inside GitHub Codespaces  

---

## ⚙️ Quick Start

### 1. Clone this repo
```bash
git clone https://github.com/stanleymay20/AutoDevAgent-GPTX
cd AutoDevAgent-GPTX

```


### 2. Install dependencies

```bash

pip install openai python-dotenv

```


### 3. Configure your API key

```bash
cp config/.env.example .env

```

Edit .env and add your OpenAI key:

```ini

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

### 4. Add a task
Edit this file:

```bash
context/current_task.txt

```

Example:

```css
Build a Flask app with login, registration, and a dashboard.

```


### 5. Add project context (optional but recommended)
Edit:
```bash
context/project_context.txt

```

Example:

```pgsql

This is a task management app using Flask + SQLite with user login. The UI uses Bootstrap.
```

### 6. Run the agent loop

```bash
python dev_agent.py

```

The agent will:

1. Ask GPT-4 to perform the task

2. Save code to logs/

3. Log response in context/task_log.txt

4. Auto-commit + push to GitHub

5. Wait and repeat



