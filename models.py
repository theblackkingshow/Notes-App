from config import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    email = db.Column(db.String(120), unique=True)

    password = db.Column(db.String(255))

    notes = db.relationship("Note", backref="user")


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    notes = db.relationship("Note", backref="category")


class Note(db.Model):

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150))

    content = db.Column(db.Text)

    created_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    category_id = db.Column(db.Integer,
                            db.ForeignKey("categories.id"))