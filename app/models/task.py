from app.extensions import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'Task "{self.title}"'
