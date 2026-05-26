import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello():
    return {"message": "Hi my dear friednd!, print higher /fact"}
@app.get("/fact")
def fact():
    return {"fact": "Cat has 9 lifes"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
