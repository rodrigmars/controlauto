from model.User import User
from infra.repositories.user_repository import UserRepository


class UserPresenter(UserRepository):

    def __init__(self) -> None:
        super().__init__()

    def insert(self, user: str, email: str, telephone: str) -> None:

        self.add(User(user, email, telephone))

    def check(self, user: str,
              email: str,
              telephone: str) -> bool:

        if user.strip().__len__() < 1:
            raise Exception("Informe nome de usuário")

        return True
