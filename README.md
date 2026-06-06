# Todo App

A beautiful, modern, and lightweight Todo web application with a FastAPI backend and a responsive vanilla CSS/JS frontend.

## Features
- **Modern & Responsive UI**: Built with a clean green color palette, custom glassmorphism effects, statistics bar, progress tracker, toast notifications, skeleton loaders, and smooth animations.
- **FastAPI Backend**: A robust Python FastAPI backend to handle data read/write locally using a JSON database (`todos.json`).
- **Hybrid Storage Support**: Automatically detects the environment. If deployed on serverless platforms like Vercel (where the file system is read-only), the application seamlessly falls back to using `localStorage` to save and manage todos directly in the browser.
- **Initial Setup Loader**: When using `localStorage` on a new device, it pre-populates the list with default todos from the repository's database on the first load.

## Tech Stack
- **Frontend**: HTML5, Vanilla CSS3 (Google Fonts: Syne, DM Sans), Javascript (ES6)
- **Backend**: Python 3.x, FastAPI, Pydantic, Uvicorn

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/nozimarustamova828-cyber/Todo-app.git
cd Todo-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the backend server
```bash
python main.py
```
Or use uvicorn:
```bash
uvicorn main:app --reload
```

### 4. Open in browser
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) or open `index.html` directly in your browser.

## Deployment

The application is fully compatible with static hosting services like **Vercel**, **GitHub Pages**, or **Netlify**. Upon deployment, it will automatically switch to client-side storage (`localStorage`) so that users can save their tasks persistently in their browser without database connectivity errors.

---
Created by [nozimarustamova828-cyber](https://github.com/nozimarustamova828-cyber)
