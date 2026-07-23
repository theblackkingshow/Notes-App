from pathlib import Path

from flask import Flask

from config import db
from models import Category, Note, User

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "notes.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return "<h1>Notes app is running</h1><p>The server is ready.</p>"


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)