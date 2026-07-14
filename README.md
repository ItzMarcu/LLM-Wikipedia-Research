# LLM Wikipedia Research

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An LLM-powered research framework designed to autonomously retrieve, analyze, and synthesize deep knowledge from Wikipedia. By leveraging Retrieval-Augmented Generation (RAG) or advanced prompting strategies, this tool extracts context-rich information to answer complex queries and compile structured reports.

## 📁 Project Structure

```text
├── backend/             # Server, LLM integration, and API logic
├── frontend/            # Web interface / User UI
├── .gitignore           # Ignored files (e.g., .venv, __pycache__)
└── README.md            # Project documentation
```

## 🚀 Features

- **Semantic Wikipedia Retrieval:** Queries Wikipedia dynamically to extract relevant contexts based on semantic similarity rather than just keyword matches.
- **Context-Grounded Generation:** Uses Large Knowledge Models (LLMs) to synthesize information, minimizing hallucinations by citing retrieved sources.
- **Interactive UI:** A user-friendly frontend to submit research topics and visualize compiled reports in real-time.
- **Clean Architecture:** Modular separation between the frontend interface and backend LLM pipeline.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI/Flask, LangChain / LlamaIndex (or your framework of choice)
- **Frontend:** HTML/CSS/JavaScript or React/Vue (depending on your implementation)
- **LLM Integration:** OpenAI API / Ollama (for local execution) / HuggingFace

## 📦 Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/ItzMarcu/LLM-Wikipedia-Research.git](https://github.com/ItzMarcu/LLM-Wikipedia-Research.git)
cd LLM-Wikipedia-Research
```

### 2. Backend Setup
Navigate to the backend directory, create a virtual environment, and install dependencies:
```bash
cd backend

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows (cmd):
.venv\Scripts\activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file inside the `backend` folder and add your configuration (e.g., API keys):
```env
OPENAI_API_KEY=your_api_key_here
# Add any other config variables needed for the project
```

### 4. Running the Application
* **Start the backend:**
  ```bash
  # Inside backend/
  python main.py  # or uvicorn main:app --reload depending on your setup
  ```
* **Start the frontend:**
  Navigate to the `frontend/` directory and open `index.html` or run your local dev server:
  ```bash
  cd ../frontend
  # e.g., if using npm:
  npm run dev
  ```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.