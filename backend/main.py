from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'klesis!'}