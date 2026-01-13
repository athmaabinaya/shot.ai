from fastapi import FastAPI

app = FastAPI(title="shot.ai API")

@app.get("/")
def health():
    return {"status": "ok", "app": "shot.ai"}
