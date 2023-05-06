import tkinter as tk
from presenter.user_presenter import UserPresenter
from model.User import User


class UserView(UserPresenter, User):

    def __init__(self, root) -> None:

        super().__init__()

        self.name_text = tk.StringVar(root, value=None)
        self.email_text = tk.StringVar(root, value=None)
        self.telephone_text = tk.StringVar(root, value=None)

        self.name_label = tk.Label(root, text="Nome")
        self.name_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.name_entry = tk.Entry(root, textvariable=self.name_text)
        self.name_entry.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.name_entry.focus()

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0, sticky='nsew')

        self.email_entry = tk.Entry(root, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=0, columnspan=2, sticky='nsew')

        self.telephone_label = tk.Label(root, text="Telefone")
        self.telephone_label.grid(row=4, column=0, sticky='nsew')

        self.telephone_entry = tk.Entry(root, textvariable=self.telephone_text)
        self.telephone_entry.grid(row=5, column=0, sticky='nsew')

        self.add_button = tk.Button(root, text="Adicionar")
        self.add_button.grid(row=6, column=0, sticky='nsew')

    def add(self) -> None:

        if self.check():

            self.insert(self.name_text.get(),
                        self.email_text.get(),
                        self.telephone_text.get())

    def remove(self) -> None:
        pass

    def check(self) -> bool:

        if self.name_text.get().strip() == "":
            self.name_entry.focus()
            # self.name_entry.configure(bg="yellow")
            return False
        return True
