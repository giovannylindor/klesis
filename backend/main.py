from fastapi import FastAPI
from database import create_db
from routers import applications
from middleware.cors import cors_middleware


app = FastAPI()
cors_middleware(app)

app.include_router(applications.router)

@app.on_event('startup')
def startup_event():
    create_db()




#@app.get('/')
#def get_root():
#    return "Klesis Backend!"

#@app.post('/user')
#def create_user(user: User, session: Session = Depends(get_session)):
    #session.add(user)
    #session.commit()
    #session.refresh(user)



