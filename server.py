from fastapi import FastAPI, HTTPException
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
async def greet_user(request: NameRequest):
    if not request.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    greeting = random.choice(greetings)
    return {"message": f"Hello {request.name}, {greeting}"}

