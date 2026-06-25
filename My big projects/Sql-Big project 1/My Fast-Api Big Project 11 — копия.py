from fastapi import FastAPI
import uvicorn
import db_manager
app = FastAPI()
@app.get("/items")
def show_items():
    return {"products": db_manager.get_all_products()}
try:
    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)
except Exception as error:
    print(f"Happend a problem {error}")


