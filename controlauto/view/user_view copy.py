import tkinter as tk
from presenter.user_presenter import UserPresenter
from model.User import User
from model.EntryPhoneNumber import EntryPhoneNumber

class UserView(UserPresenter, User):

    def __init__(self, root) -> None:

        super().__init__()

        self.BACKGROUND_YELLOW:dict = {"background": "yellow"}
        self.FOREGROUND_YELLOW:dict = {"foreground": "red"}

        self.BACKGROUND_DEFAULT:dict = {"background": "white"}
        self.FOREGROUND_DEFAULT:dict = {"foreground": "black"}
        # configure(text_font = ('verdana', 8)

        self.frmUser = tk.Frame(root, pady=50)
        self.frmUser.pack()

        # Variables
        self.name_text = tk.StringVar(self.frmUser, value=None)
        self.email_text = tk.StringVar(self.frmUser, value=None)
        self.telephone_text = tk.StringVar(self.frmUser, value=None)

        # Nome
        self.name_label = tk.Label(self.frmUser, text="Nome")
        self.name_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.name_entry = tk.Entry(self.frmUser, textvariable=self.name_text, width=35)
        self.name_entry.grid(row=1, column=0, sticky='nsew')
        self.name_entry.focus()

        self.name_entry.bind("<Key>", self.event_key)


        self.name_notify = tk.Label(self.frmUser, text="*")
        self.name_notify.grid(row=1, column=1, sticky='nsew')

        # Email
        self.email_label = tk.Label(self.frmUser, text="Email")
        self.email_label.grid(row=2, column=0, columnspan=2, sticky='nsew')

        self.email_entry = tk.Entry(self.frmUser, textvariable=self.email_text, width=5)
        self.email_entry.grid(row=3, column=0, sticky='nsew')

        self.email_notify = tk.Label(self.frmUser, text="*")
        self.email_notify.grid(row=3, column=1, sticky='nsew')

        # Telefone
        self.telephone_label = tk.Label(self.frmUser, text="Telefone")
        self.telephone_label.grid(row=4, column=0, columnspan=2, sticky='nsew')

        # self.telephone_entry = tk.Entry(
        #     self.frmUser, textvariable=self.telephone_text)
        # self.telephone_entry.grid(row=5, column=0, sticky='nsew')

        self.telephone_entry = EntryPhoneNumber(self.frmUser,
                                                placeholder='(000)-1111-111111',
                                                textvariable=self.telephone_text)

        self.telephone_entry.grid(row=5, column=0, sticky='nsew')

        self.telephone_notify = tk.Label(self.frmUser, text="*")
        self.telephone_notify.grid(row=5, column=1, sticky='nsew')

        # Button
        self.add_button = tk.Button(
            self.frmUser, text="Adicionar", command=self.add)
        self.add_button.grid(row=6, column=0, columnspan=2, sticky='nsew', pady=20)

        self.digits: str = ""

    def digits_set(self, key: str) -> None:
        self.digits += key

    def digits_get(self) -> str:
        return self.digits

    def event_key(self, event):

        digit = str(event.char)

        print("name_text:", self.name_text.get())

        if (len(self.name_text.get()) <= 9):
            return exit

        

        # self.digits_set(self.name_text.get())

        # print("pressed", self.digits_get())


    def add(self) -> None:

        if self.check():
            # self.insert(self.name_text.get(),
            #             self.email_text.get(),
            #             self.telephone_text.get())
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