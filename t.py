from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat/{room}",responseType=HTMLResponse)
async def chatroom(room):
    return open("chatlog").read()
class msg(BaseModel):
  user:str
  message:str

@app.post("/chat/{room}")
async def chatroom(room,message:msg):
     open("chatlog","a").write(message.user+":"+message.message)