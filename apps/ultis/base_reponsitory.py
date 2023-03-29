from apps.ultis.const import LIMIT, PAGE
from extensions.database import db


class BaseRepository:
    def __init__(self, model: db.Model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, id):
        return self.model.query(self.model.id == id).first()

    def filter(self):
        return self.model.query

    @staticmethod
    def pagination(query_set, page: int = PAGE, limit: int = LIMIT):
        return query_set.paginate(page=page, per_page=limit)
