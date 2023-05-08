import tkinter as tk


class NameComponent(tk.Entry):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.digits: str = ""

        self.bind("<KeyPress>", self.onKeyDown)
        self.bind("<BackSpace>", self.onBackSpace)

    def get_digits(self) -> str:
        return self.digits

    def set_digits(self, digit: str) -> None:
        self.digits = digit

    def onKeyDown(self, event):

        if len(self.get_digits()) >= 5:
            return "break"

        self.set_digits(self.get_digits() + str(event.char))

    def onBackSpace(self, _: object):
        self.set_digits(self.get_digits()[:-1:])
