import tkinter as tk


class NameEntryComponent(tk.Entry):

    def __init__(self, min_digits:int, max_digits: int,  *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.min_digits = min_digits
        self.total_digits = max_digits
        self.digits: str = ""

        self.bind("<KeyPress>", self.onKeyDown)
        self.bind("<BackSpace>", self.onBackSpace)

    def get_digits(self) -> str:
        return self.digits

    def set_digits(self, digit: str) -> None:
        self.digits = digit

    def onKeyDown(self, event):

        if str(event.char).isalpha() is not True:
            return "break"

        if len(self.get_digits()) >= self.total_digits:
            return "break"

        self.set_digits(self.get_digits() + str(event.char))

    def onBackSpace(self, _: object):
        self.set_digits(self.get_digits()[:-1:])
