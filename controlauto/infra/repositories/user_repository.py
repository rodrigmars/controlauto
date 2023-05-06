from infra.repositories.repository import Repository
from model.User import User


class UserRepository(Repository):

    def __init__(self) -> None:
        super().__init__()

    def add(self, user: User):
        pass
