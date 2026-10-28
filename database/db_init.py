from main import app
from .exts import db


with app.app_context():
    db.create_all()
    print("Database created")