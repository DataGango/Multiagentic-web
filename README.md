# AI Web Agent

This is a Python-based AI web agent that uses the Gemini API to generate modern, dynamic UI websites based on natural language prompts. It also includes an automated test script to render the site and take a screenshot.

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   cd /Users/poulomigangopadhyay/webagent
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Set your Gemini API key:**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

## Usage

### 1. Generate a Website
Run the agent with a prompt describing the website you want to generate:

```bash
python agent.py "A modern landing page for an AI startup with a dark theme, glassmorphism, and neon purple accents"
```

The generated website will be saved as `index.html` in the `output/` directory.

### 2. Test the Generated Website
Run the test script to launch a headless browser, verify the page renders, and capture a screenshot:

```bash
python test_agent.py
```

The screenshot will be saved to `output/screenshot.png`. You can also open `output/index.html` manually in your browser to view the interactive result!
