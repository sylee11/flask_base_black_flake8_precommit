from ...ultis.base_reponsitory import BaseRepository
from ..models.users import Users


class UserRepository(BaseRepository):
    pass


user_repo = UserRepository(Users)
