from ..models.users import Users
from ..ultis.base_reponsitory import BaseRepository


class UserRepository(BaseRepository):
    def get_by_email(self, email):
        return self.model.query.filter(self.model.email == email).first()


user_repo = UserRepository(Users)
