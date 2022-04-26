import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("load:app", reload=True, port=5000, host="0.0.0.0")
