from fastapi import FastAPI, HTTPException, status, Depends
from database import create_db
from models import User, Application, Interview
from database import create_db, get_session
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound
from datetime import datetime, timezone

app = FastAPI()

@app.on_event('startup')
def startup_event():
    create_db()

@app.get('/')
def get_root():
    return "Klesis Backend!"

@app.get('/form/')
def get_form(id: str, session: Session = Depends(get_session)):
    try:
        query = select(Application).where(Application.id == id)
        user_app = session.exec(query).first()
        return user_app
    except NoResultFound:
        raise HTTPException(status_code=404, detail='App not found!')
        

@app.put('/form/')
def update_form(new_app: Application, id: str, session: Session = Depends(get_session)):
    try:
        query = select(Application).where(Application.user_id == id)
        result = session.exec(query)
        form = result.one()

        form.applied_at = new_app.applied_at
        form.company = new_app.company
        form.role = new_app.role
        form.application_status = new_app.application_status
        form.url = new_app.url
        form.application_updated = datetime.now(timezone.utc)

        session.add(form)
        session.commit()
        session.refresh(form)

        return "Form Edited!"
    except NoResultFound:
        raise HTTPException(status_code=404, detail='App not found!')
    

#@app.post('/user')
#def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)

@app.post('/form/')
def create_form(application: Application, session: Session = Depends(get_session)):
    session.add(application)
    session.commit()
    session.refresh(application)    

