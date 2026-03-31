# Quick Start Guide

## Getting Started with AI Studio Mobile

### Prerequisites
- Node.js v14+
- Python 3.8+
- Git

### Installation

```bash
git clone https://github.com/peymargh/ai-studio-mobile.git
cd ai-studio-mobile
npm install
```

### Configuration

1. Copy environment file:
```bash
cp .env.example .env
```

2. Add your Hugging Face API key to `.env`

### Running Locally

```bash
# Terminal 1 - Backend
cd backend
python -m uvicorn app.main:app --reload

# Terminal 2 - Frontend
cd mobile-app
npm start
```