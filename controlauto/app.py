import tkinter as tk
from Core.User import User


class UserView(User):

    def __init__(self, root) -> None:

        self.name_text = tk.StringVar(root, value=None)
        self.email_text = tk.StringVar(root, value=None)
        self.telephone_text = tk.StringVar(root, value=None)

        self.name_label = tk.Label(root, text="Nome")
        self.name_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.name_entry = tk.Entry(root, textvariable=self.name_text)
        self.name_entry.grid(row=1, column=0, columnspan=2, sticky='nsew')

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

        User(self.name_text.get(),
             self.email_text.get(),
             self.telephone_text.get())

    def remove(self) -> None:
        pass


def main() -> None:

    root = tk.Tk()

    root.geometry('540x640')

    root.minsize(540, 640)

    root.title("controlauto 1.0.0")

    UserView(root)

    root.mainloop()


if __name__ == "__main__":

    try:

        main()

    except Exception as ex:

        print(ex)
