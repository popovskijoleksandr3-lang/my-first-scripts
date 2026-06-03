from fastapi import FastAPI
import uvicorn
app = FastAPI()
my_words = ["Python", "C++", "C+", "Java script"]
@app.get("/word/{index}")
async def get_word(index:int):
    try:
        return {"word": my_words[index]}
    except IndexError:
        return {"error": "Такго слова немає!"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")


