from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/hello")
def hello(name: str = "Гість"): # Якщо name не вкажуть, буде "Гість"
    return {"message": f"Привіт, {name}!"}
uvicorn.run(app, host="127.0.0.1", port=7000)