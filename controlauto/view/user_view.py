import tkinter as tk
from presenter.user_presenter import UserPresenter
from model.User import User


class UserView(UserPresenter, User):

    def __init__(self, root) -> None:

        super().__init__()

        # configure(text_font = ('verdana', 8)

        self.frmUser = tk.Frame(root, pady=50)
        self.frmUser.pack()

        self.name_text = tk.StringVar(self.frmUser, value=None)
        self.email_text = tk.StringVar(self.frmUser, value=None)
        self.telephone_text = tk.StringVar(self.frmUser, value=None)

        self.name_label = tk.Label(self.frmUser, text="Nome")
        self.name_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.name_entry = tk.Entry(self.frmUser, textvariable=self.name_text)
        self.name_entry.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.name_entry.focus()

        self.name_notify = tk.Label(self.frmUser, text="*")
        self.name_notify.grid(row=1, column=1, sticky='nsew')


        self.email_label = tk.Label(self.frmUser, text="Email")
        self.email_label.grid(row=2, column=0, sticky='nsew')

        self.email_entry = tk.Entry(self.frmUser, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=0, columnspan=2, sticky='nsew')

        self.email_notify = tk.Label(self.frmUser, text="*")
        self.email_notify.grid(row=3, column=1, sticky='nsew')

        self.telephone_label = tk.Label(self.frmUser, text="Telefone")
        self.telephone_label.grid(row=4, column=0, sticky='nsew')

        self.telephone_entry = tk.Entry(self.frmUser, textvariable=self.telephone_text)
        self.telephone_entry.grid(row=5, column=0, sticky='nsew')

        self.telephone_notify = tk.Label(self.frmUser, text="*")
        self.telephone_notify.grid(row=5, column=1, sticky='nsew')


        self.add_button = tk.Button(self.frmUser, text="Adicionar", command=self.add)
        self.add_button.grid(row=6, column=0, sticky='nsew')

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
            # self.name_entry.configure(bg="yellow")
            return False

        # if self.name_text.get().__len__() < 1:
        #     self.name_entry.focus()
        #     # self.name_entry.configure(bg="yellow")
        #     return False

        return True

    def disable(self):
        pass
        # self.B2.configure(state=tk.DISABLED, background='cadetblue')
        # self.Focus.configure(state=tk.DISABLED, background='cadetblue')

    def enable(self):
        pass
        # self.B2.configure(state=tk.NORMAL,
        #                   background=self.B1.cget('background'))
        # self.Focus.configure(state=tk.NORMAL,

        #                      background=self.B1.cget('background'))

    def clear(self):
        self.name_text.set("")
        self.email_text.set("")
        self.telephone_text.set("")
