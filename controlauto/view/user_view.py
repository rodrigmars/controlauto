import tkinter as tk
from tkinter import messagebox
from presenter.user_presenter import UserPresenter
from model.User import User
from model.EntryPhoneNumber import EntryPhoneNumber
from components.NameComponent import NameEntry, NameLabel


class UserView(tk.Frame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.BACKGROUND_YELLOW: dict = {"background": "yellow"}
        self.FOREGROUND_YELLOW: dict = {"foreground": "red"}

        self.BACKGROUND_DEFAULT: dict = {"background": "white"}
        self.FOREGROUND_DEFAULT: dict = {"foreground": "black"}
        # configure(text_font = ('verdana', 8)

        # Variables
        self.name_text = tk.StringVar(self, value=None)
        self.email_text = tk.StringVar(self, value=None)
        self.telephone_text = tk.StringVar(self, value=None)

        # Nome
        self.name_label = NameLabel(self, text="Nome")
        self.name_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.name_entry = NameEntry(self, textvariable=self.name_text,
                                    width=35)

        self.name_entry.grid(row=1, column=0, sticky='nsew')
        self.name_entry.focus()

        self.name_notify = tk.Label(self, text="*")
        self.name_notify.grid(row=1, column=1, sticky='nsew')

        self.name_message_label = NameLabel(self)
        self.name_message_label.grid(row=2, column=2, columnspan=2, sticky='nsew')

        # self.name_label_message = NameLabel(self, text="Erro message")
        # self.name_label_message.grid(row=, column=0, columnspan=2, sticky='nsew')



        # Email
        self.email_label = tk.Label(self, text="Email")
        self.email_label.grid(row=4, column=0, columnspan=2, sticky='nsew')

        self.email_entry = tk.Entry(
            self, textvariable=self.email_text, width=5)
        self.email_entry.grid(row=5, column=0, sticky='nsew')

        self.email_message_label = tk.Label(self, text="Email")
        self.email_message_label.grid(row=6, column=0, columnspan=2, sticky='nsew')

        # Telefone
        self.telephone_label = tk.Label(self, text="Telefone")
        self.telephone_label.grid(row=7, column=0, columnspan=2, sticky='nsew')

        # self.telephone_entry = tk.Entry(
        #     textvariable=self.telephone_text)
        # self.telephone_entry.grid(row=5, column=0, sticky='nsew')

        self.telephone_entry = EntryPhoneNumber(self,
                                                placeholder='(000)-1111-111111',
                                                textvariable=self.telephone_text)

        self.telephone_entry.grid(row=8, column=0, sticky='nsew')

        self.telephone_notify = tk.Label(self, text="*")
        self.telephone_notify.grid(row=9, column=1, sticky='nsew')

        # Button
        self.add_button = tk.Button(self, text="Adicionar",
                                    command=self.add)

        self.add_button.grid(row=11,
                             column=0,
                             columnspan=2,
                             sticky='nsew',
                             pady=20)

        self.digits: str = ""

    def digits_set(self, key: str) -> None:
        self.digits += key

    def digits_get(self) -> str:
        return self.digits

    def add(self) -> None:

        if self.check():
            # self.insert(self.name_text.get(),
            #             self.email_text.get(),

            #             self.telephone_text.get())
            messagebox.showwarning(title="Cadastro Usuário", message="Usuário cadastrado com sucesso")
            self.clear()

    def remove(self) -> None:
        pass

    def check(self) -> bool:

        if self.name_text.get().strip() == "":
            self.name_entry.focus()
            self.name_entry.configure(**self.BACKGROUND_YELLOW)
            self.name_notify.configure(**self.FOREGROUND_YELLOW)
            return False

        # if self.name_text.get().__len__() < 1:
        #     self.name_entry.focus()
        #     # self.name_entry.configure(bg="yellow")
        #     return False
        self.reset()
        return True

    def disable(self):
        pass

    def enable(self):
        pass

    def reset(self):

        self.name_entry.configure(**self.BACKGROUND_DEFAULT)
        self.email_entry.configure(**self.BACKGROUND_DEFAULT)
        self.telephone_entry.configure(**self.BACKGROUND_DEFAULT)

        self.name_notify.configure(**self.FOREGROUND_DEFAULT)
        self.email_notify.configure(**self.FOREGROUND_DEFAULT)
        self.telephone_notify.configure(**self.FOREGROUND_DEFAULT)

    def clear(self):
        self.name_text.set("")
        self.email_text.set("")
        self.telephone_text.set("")
