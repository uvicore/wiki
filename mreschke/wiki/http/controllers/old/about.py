from uvicore import app, config, http
from uvicore.http import Router, controller, render
#from mreschke.wiki.models.user import User
#from fastapi import Depends

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Response
from fastapi.responses import HTMLResponse

#from mreschke.wiki import db

# New router for this controller
route = Router()


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import sqlalchemy as sa
# from sqlalchemy.orm import Session
# from pydantic import BaseModel as Schema
# from functools import lru_cache
# from fastapi_utils.session import FastAPISessionMaker
# from typing import Iterator

#engine = create_engine("mysql+pymysql://root:techie@127.0.0.1/uvicore_wiki")
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()

# class User(Base):
#     __tablename__ = "user"
#     id = sa.Column(sa.Integer, primary_key=True)
#     name = sa.Column(sa.String(length=50))

# class UserSchema(Schema):
#     id: int
#     name: str

#     class Config:
#         orm_mode = True





# Dependency
# def get_db():
#     x = SessionLocal()
#     #x = session()
#     try:
#         yield x
#     finally:
#         x.close()

# def get_db() -> Iterator[Session]:
#     """ FastAPI dependency that provides a sqlalchemy session """
#     yield from _get_fastapi_sessionmaker().get_db()

# @lru_cache()
# def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
#     """ This function could be replaced with a global variable if preferred """
#     database_uri = "mysql+pymysql://root:techie@127.0.0.1/uvicore_wiki"
#     return FastAPISessionMaker(database_uri)

# Does my template overrides for me !!!.  First one defined WINS
templates = Jinja2Templates(directory=["mreschke/wiki/http/views2", "mreschke/wiki/http/views"])


# Class based Controller
@controller(route)
class About:

    @route.get('/about')
    def about(self, request: Request):
        #return {'Page': 'About'}
        #return Response(content=templates.TemplateResponse('about.j2', {'request': request}), media_type="text/html")
        html = "<b>Hi</b> there"
        #return Response(content=html, media_type="text/html")
        return HTMLResponse(content=html, status_code=200)

        #return render('about.j2')

    # @route.get('/about2')
    # def about2(self, db: Session = Depends(get_db)):
    #     #return {'Page': 'About'}
    #     #return User.query.all()
    #     #return db.query(User).all()
    #     #return get_users(db)
    #     return db.query(User).all()

