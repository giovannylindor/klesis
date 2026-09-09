from fastapi import HTTPException, status, Depends, APIRouter
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import NoResultFound
from database import get_session
from models import Application
from datetime import datetime, timezone

router = APIRouter(prefix='/application', tags=['applications'])


@router.get('/')
def get_form(id: str, session: Session = Depends(get_session)):
    try:
        query = select(Application).where(Application.id == id)
        user_app = session.exec(query).first()
        return user_app
    except NoResultFound:
        raise HTTPException(status_code=404, detail='App not found!')


@router.put('/')
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


@router.post('/')
def create_form(application: Application, session: Session = Depends(get_session)):
    session.add(application)
    session.commit()
    session.refresh(application)    