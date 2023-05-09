import tkinter as tk


class NameLabel(tk.Label):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)


class NameEntry(tk.Entry):

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.min_length = kwargs["min_length"]
        self.max_length = kwargs["max_length"]
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

        if len(self.get_digits()) >= self.max_length:
            return "break"

        self.set_digits(self.get_digits() + str(event.char))

    def onBackSpace(self, _: object):
        self.set_digits(self.get_digits()[:-1:])
