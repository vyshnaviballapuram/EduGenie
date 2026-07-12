# EduGenie — Google Gemini Powered Learning Assistant

Project built for the **SmartBridge Google Cloud Gen AI Internship**.

EduGenie is an AI-powered learning assistant that helps students with:
- **Question Answering** (Gemini 1.5 Pro)
- **Concept Explanation** (LaMini-Flan-T5-783M, local lightweight model)
- **Quiz Generation** (Gemini 1.5 Pro, MCQs in JSON)
- **Text Summarization** (Gemini 1.5 Pro)
- **Personalized Learning Path Recommendations** (Gemini 1.5 Pro)

## Folder Structure

```
edugenie/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── explanation_module.py
├── learning_path.py
├── main.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup

1. **Clone the repo & create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your Gemini API key**
   - Copy `.env.example` to `.env`
   - Get a key from [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)
   - Add it to `.env`:
     ```
     GEMINI_API_KEY=your_actual_key
     ```

4. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser at **http://127.0.0.1:8000**

## API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/qa?question=...` | Ask a question, answered via Gemini |
| POST | `/explain/` | `{ "topic": "..." }` → simplified explanation |
| POST | `/summarize/` | `{ "text": "..." }` → summary |
| POST | `/quiz` | `{ "text": "..." }` → 3 MCQs (JSON) |
| GET | `/learn/recommendations?topic=...` | Personalized learning path |

## Tech Stack

- **Backend:** FastAPI, Uvicorn
- **AI Models:** Google Gemini 1.5 Pro (cloud), LaMini-Flan-T5-783M (local, via Hugging Face Transformers)
- **Frontend:** HTML, CSS, Jinja2, vanilla JS (fetch API)

## Notes

- `explanation_module.py` downloads `MBZUAI/LaMini-Flan-T5-783M` from Hugging Face on first run — this may take a few minutes.
- Do **not** commit your `.env` file or API key to the repository.
