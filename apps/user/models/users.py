"""
please import models to ./migrations/env.py to Flask Migrate working
"""
from extensions.database import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(
        db.String(128), nullable=False, unique=True, name="email"
    )
    company_name = db.Column(
        db.String(200), nullable=False, unique=False, name="companyName"
    )
