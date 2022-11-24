from extensions.database import db


class BaseRepository:
    def __init__(self, model: db.Model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, id):
        return self.model.query(self.model.id == id).first()
