from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root(username: str = Query("Guest")):
    return {"message": f"Welcome {username}!"}
