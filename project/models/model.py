"""Data models."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app=app)
    app.db = db

    
    
class User(db.Model):
    """Data model for user accounts."""
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    cpf = db.Column(
        db.String(11),
        index=True,
        unique=True,
        nullable=True
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    phone = db.Column(
        db.String(11),
        index=True,
        unique=True,
        nullable=True
    )
    street = db.Column(
        db.Text,
        index=True,
        unique=True,
        nullable=True
    )
    password = db.Column(
        db.Text,
        index=True,
        unique=True,
        nullable=False
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

class WishList(db.Model):
    """Data model for user WishList."""
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    id_user = db.Column(
        db.Integer,
        index=False,
        unique=True,
        nullable=False
    )
    production = db.Column(
        db.Text,
        index=False,
        unique=True,
        nullable=False
    )
    cash = db.Column(
        db.Float,
        index=True,
        unique=True,
        nullable=True
    )
    create = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    payment = db.Column(
        db.Text,
        index=True,
        unique=True,
        nullable=False
    )
    total = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )

class Productions(db.Model):
    """Data model for user Productions."""
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    description = db.Column(
        db.Text,
        index=True,
        unique=False,
        nullable=True
    )
    create = db.Column(
        db.DateTime,
        index=True,
        unique=True,
        nullable=True
    )
    cash = db.Column(
        db.Float,
        index=True,
        unique=False,
        nullable=False
    )
    category = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    image = db.Column(
        db.Text,
        index=True,
        unique=True,
        nullable=True
    )


class category(db.Model):
    """Data model for user category."""
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.Text,
        index=False,
        unique=True,
        nullable=False
    )