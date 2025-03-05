from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import random

app = FastAPI()

# List of 50 different greeting variations
greetings = [
    "Hope you're having a fantastic day!", "Nice to meet you!", "Wishing you all the best!",
    "Stay awesome!", "Keep smiling!", "You're amazing!", "Have a great time!", "Enjoy your day!",
    "Wishing you success!", "Make today special!", "Stay positive!", "Have fun today!",
    "You rock!", "Keep shining!", "Sending good vibes!", "Stay cheerful!", "Enjoy every moment!",
    "Take care!", "Spread kindness!", "Seize the day!", "Happiness is yours!", "Keep being awesome!",
    "Live, laugh, love!", "You’re doing great!", "Believe in yourself!", "Follow your dreams!",
    "Have a fantastic time!", "Smile often!", "Dream big!", "Good things are coming your way!",
    "Stay confident!", "May your day be bright!", "Embrace the adventure!", "Go for it!",
    "Stay strong!", "Make it count!", "You’ve got this!", "Shine on!", "Love what you do!",
    "Laugh a lot!", "Think positively!", "Keep learning!", "Be fearless!", "Have a blast!",
    "You inspire others!", "Success is near!", "The world needs you!", "Live boldly!",
    "Enjoy the little things!", "Make a difference!"
]

class NameRequest(BaseModel):
    name: str

@app.post("/greet")
async def greet_user(request: Request, name_request: NameRequest):
    if request.headers.get("content-type") != "application/json":
        raise HTTPException(status_code=400, detail="Content-Type must be application/json.")
    if not name_request.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    greeting = random.choice(greetings)
    return {"message": f"Hello {name_request.name}, {greeting}"}

@app.get("/help")
async def help():
    return {
        "message": "To use the /greet endpoint, send a POST request with Content-Type: application/json header and a JSON body containing a 'name' field. Example: {\"name\": \"YourName\"}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6767)

