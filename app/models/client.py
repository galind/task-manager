from app.extensions import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f'Task "{self.name}"'
