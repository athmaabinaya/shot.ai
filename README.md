# shot.ai
a shot glass holds a lot more than you think.

shot.ai is a mobile-first, AI-curated daily digest of emerging technology,
developer tools, and AI trends.

Instead of infinite feeds, shot.ai delivers a concise daily “shot” of
high-signal insights — summarized, categorized, and readable directly
inside the app.

## Core principles
- Signal over noise
- In-app reading, not link dumping
- AI as an editor, not a hype machine
- Built for engineers who want to stay sharp

## Tech Stack (initial)
- Mobile: Flutter
- Backend: FastAPI (Python)
- AI: Gemini Flash (latest) for fast, cost-efficient daily summaries
- Data: PostgreSQL

### Install

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

cd ../mobile/shot_ai
flutter pub get
flutter run -d windows

