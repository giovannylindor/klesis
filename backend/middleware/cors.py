from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

DEV_URL = os.getenv('DEVELOPMENT_URL')


def cors_middleware(app: FastAPI):
    app.add_middleware(CORSMiddleware, 
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_origins=[DEV_URL],
                       allow_headers=['*'])


