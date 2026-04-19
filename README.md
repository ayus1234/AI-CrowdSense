# 🧠 AI CrowdSense - Smart Event Experience Platform

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Google Gemini](https://img.shields.io/badge/Google%20GenAI-Gemini_Flash-orange)](https://aistudio.google.com/)

### 🔴 **[Live Demo: Play with AI CrowdSense Online](https://ai-crowdsense-15593284604.europe-west1.run.app)** 🔴

**AI CrowdSense** is a smart, real-time venue navigation and queue prediction system designed to dramatically improve the attendee experience at large-scale events (sports stadiums, concerts, airports, and malls).

## 📸 Application Interface
<div align="center">
  <img src="assets/dashboard.png" width="48%" alt="Dashboard Overview" />
  <img src="assets/ai_assistant.png" width="48%" alt="AI Assistant Conversation" />
</div>

## 🏆 Problem Addressed
At large sporting events, attendees waste enormous amounts of time stuck in bottlenecks, standing in massive queues for food or washrooms, and struggling to navigate. This leads to frustrated fans and unequal distribution of crowds for vendors.

## 🚀 Our Solution
**AI CrowdSense** fixes this chaos by actively analyzing crowd density and providing intelligent recommendations via Google Gemini's advanced LLM.
1. **🧭 Smart Navigation:** Dynamically updates routes to avoid physical bottlenecks.
2. **⏱ Live Queue Prediction:** Re-routes fans dynamically based on which food stalls have the shortest waiting times.
3. **🤖 Automated AI Assistant:** Acts as a proactive "traffic controller", answering user questions while implementing **Bias-Aware route balancing** to prevent creating *new* bottlenecks at popular vendors.

## ✨ Features
* **Premium Glassmorphism UI:** Stunning, responsive front-end designed to wow judges and users alike.
* **Bias-Aware Recommendation Logic:** Doesn't just blindly send everyone to the shortest queue. Gemini actively distributes traffic to balance the crowd flow across the entire venue.
* **Live Simulated Data Engine:** Replicates real-time stadium metrics on a backend loop.
* **Dynamic Animations:** Features an AI welcome message typing effect, engineered AI 'thinking' delays for premium UX, interactive queue row hovers, custom pulsing 'LIVE' badges, and bright projector-optimized contrast styling.
* **Fully Responsive:** Beautifully adapts from 4K ultrawide monitors down to 400px mobile phones.

## 🛠️ Technology Stack
* **Frontend Layer:** HTML5, CSS3, Vanilla JavaScript
* **Backend Framework:** Python FastAPI
* **AI Integration:** Google GenAI / Gemini 2.5 Flash API
* **Deployment System:** Cloud native, Dockerized for Google Cloud Run (Single-container architecture)

## 💻 Running the App Locally

### 1. Prerequisites Ensure you have Python 3.10+ installed.

### 2. Add API Key
Create a `.env` file in the root directory and add your Google Studio API key:
```ini
GEMINI_API_KEY="your-api-key-here"
```

### 3. Install Requirements
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 4. Run the Engine
```bash
python backend/app.py
```
*Navigate to `http://localhost:8080` to interact with the live CrowdSense Dashboard!*

---
*Built for the 2026 AI Innovation Hackathon. Stop standing in lines, start enjoying the event.*
