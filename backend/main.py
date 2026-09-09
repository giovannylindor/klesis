from fastapi import FastAPI, HTTPException, status
from database import create_db

app = FastAPI()

@app.on_event('startup')
def startup_event():
    create_db()

@app.get('/')
def get_root():
    return {'message': 'klesis!'}