class User:
    def __init__(self, name: str, email: str, telephone: str) -> None:
        self.name = name
        self.email = email
        self.telephone = telephone

    def name_get(self) -> str:
        return self.name

    def name_set(self, name: str) -> None:
        self.name = name

    def email_get(self) -> str:
        return self.email

    def email_set(self, email: str) -> None:
        self.email = email

    def telephone_get(self) -> str:
        return self.telephone

    def telephone_set(self, telephone: str) -> None:
        self.telephone = telephone
