from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel):
    id: str | None = Field(default=None, primary_key=True)
    email: str | None = Field(default=None, nullable=False)
    name: str | None = Field(default=None, nullable=False)
    aspiring_role: str | None = Field(default=None, nullable=True)
    account_created: datetime | None = Field(default=None, nullable=True)


class Application(SQLModel):
    id: int | None = Field(primary_key=True, default=None)
    user_id: str | None = Field(default=None, foreign_key='user.id')
    company: str | None = Field(default=None, nullable=False)
    role: str | None = Field(default=None, nullable=False)
    application_status: str | None = Field(default=None, nullable=False)
    url: str | None = Field(default=None, nullable=True)
    applied_at: datetime | None = Field(default=None, nullable=False)
    application_created: datetime | None = Field(default=None, nullable=False)
    application_updated: datetime | None = Field(default=None, nullable=False)


class Interview(SQLModel):
    id: int | None = Field(primary_key=True, default=None)
    interview_date: datetime | None = Field(default=None, nullable=False)
    notes: str | None = Field(default=None, nullable=True)