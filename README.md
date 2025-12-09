## Multi-Agent Math System

A small demo that routes math questions to different “agents” (school, college, university) using Google Gemini models. The entry point is `main.py`.

### Setup
- Install dependencies (inside your virtual env):
  ```bash
  pip install -r requirements.txt
  ```
- Create a `.env` file with your Gemini API key (and optional model override):
  ```
  GEMINI_API_KEY=your-key-here
  GEMINI_MODEL=models/gemini-2.0-flash  # optional; falls back through a few defaults
  ```

### Run
```bash
python main.py
```
You’ll see test cases printed with the assigned agent and solution.

### Notes
- If you see a 404 “model not found”, set `GEMINI_MODEL` to a model your key supports (run a quick list with `python -c "import google.generativeai as genai, os; genai.configure(api_key=os.getenv('GEMINI_API_KEY')); [print(m.name) for m in genai.list_models()]"`).
- If you hit quota errors (429), wait for the retry window or enable billing / increase limits in your Google Cloud project.
