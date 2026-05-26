from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/car/{car_id}")
def get_car(car_id: int):
    return {"car_id": car_id, "info": f"car with id {car_id} is fast"}
if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)