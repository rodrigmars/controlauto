import tkinter as tk


class EntryPhoneNumber(tk.Entry):

    def __init__(self, master=None,
                 placeholder='',
                 cnf={},
                 fg='black',
                 fg_placeholder='grey50',
                 *args, **kw):

        super().__init__(master=master, cnf={}, bg='white', *args, **kw)

        self.fg = fg
        self.fg_placeholder = fg_placeholder
        self.placeholder = placeholder
        # self.bind('<FocusOut>', self.fill_placeholder())
        self.bind('<FocusIn>', self.clear_box())
        self.fill_placeholder()

    def clear_box(self):
        if not self.get() and super().get():
            print("chegando aqui")
            self.config(fg=self.fg)
            self.delete(0, tk.END)

    def fill_placeholder(self):
        print(">>>>>>", len(super().get()), super().get())
        if not super().get():
            print("chegando aqui22")
            self.config(fg=self.fg_placeholder)
            self.insert(0, self.placeholder)

    def get(self):
        content = super().get()

        if content == self.placeholder:
            return ''

        return content
