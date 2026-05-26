import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def calculate():
    result = 10 + 5
    return {"calculation": "10 + 5", "result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)
