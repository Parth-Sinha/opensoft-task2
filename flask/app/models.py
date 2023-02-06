from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, CHAR


from app import app

db = SQLAlchemy(app)

class Classroom(db.Model):
    __tablename__ = 'students'

    serial_no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(CHAR (40))
    roll_no = Column(CHAR (9))
    department= Column(CHAR (2))
