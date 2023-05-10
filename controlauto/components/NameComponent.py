import tkinter as tk


class NameLabel(tk.Label):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)


class NameEntry(tk.Entry):

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.min_length = 5
        self.max_length = 10
        self.digits: str = ""

        self.bind("<KeyPress>", self.on_key_down)
        self.bind("<BackSpace>", self.on_back_space)
        self.bind("<Tab>", self.on_focus)
        # self.bind("<Key>", self.on_click)
        # self.bind('<<Modified>>', self.on_modified)

        self.log_message = tk.Label(self, text="")

    def on_click(self, _):
       position = self.index(tk.INSERT)
       self.icursor(position - 1)

    def on_focus(self, event):
        event.widget.tk_focusNext().focus()
        return ("break")

    def get_min_length(self) -> int:
        return self.min_length

    def get_max_length(self) -> int:
        return self.max_length

    def get_digits(self) -> str:
        return self.digits

    def set_digits(self, digit: str) -> None:
        self.digits = digit

    def on_key_down(self, event):

        self.icursor(tk.END)

        if str(event.char).isalpha() is not True:
            return "break"

        if len(self.get_digits()) >= self.get_max_length():
            return "break"

        self.set_digits(self.get_digits() + str(event.char))

    def on_back_space(self, _: tk.Event):

        self.icursor(tk.END)

        if self.select_present():
            self.select_clear()
            return "break"

        self.set_digits(self.get_digits()[:-1:])

        # else:
        #     self.set_digits(self.get_digits()[:-1:])

    # def on_focus_out(self, event) -> object:

    #     if len(self.get_digits()) <= self.get_min_length():
    #         self.log_message.configure(row)
    #         self.configure(bg="yellow")
    #         return "break"
