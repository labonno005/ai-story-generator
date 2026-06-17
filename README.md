# AI Story Generator API 🎯

An AI-powered Story Generation API built using **FastAPI**, **OpenAI API**, and **Docker**.

This project generates creative short stories from a single-line prompt.

---

## 🚀 Features

- Generate AI-based stories from prompts
- FastAPI backend (high performance)
- OpenAI integration
- Clean API structure (modular design)
- Docker support
- Swagger UI documentation (/docs)

---

## 🧠 How It Works

User sends a prompt → API processes it → OpenAI generates story → Response is returned.

---

## 📁 Project Structure

ai-story-generator/
│
├── app/ 
│
│ ├── main.py 
│
│ ├── Story/ 
│ │
│ │ ├── story.py 
│ │ ├── openai_service.py 
│ │ └── story_schema.py 
│
│ ├── core/
│ │
│ │ └── config.py 
│
│ └── utils/ 
│ └── prompt_template.py 
│
├── .env
├── .gitignore 
├── requirements.txt 
├── Dockerfile
├── docker-compose.yml
└── README.md

---