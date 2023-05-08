import tkinter as tk
from view.user_view import UserView


def main() -> None:

    root = tk.Tk()

    root.geometry('540x640')

    root.minsize(540, 640)

    root.title("controlauto 1.0.0")

    root.resizable(False, False)

    # UserView(root)

    from components.NameComponent import NameComponent 

    # font=('calibre',10,'normal')

    name = NameComponent(master=root, fg="red")

    name.grid(row=0, column=0)

    # def fetch(entries):
    #     for entry in entries:
    #         field = entry[0]
    #         text = entry[1].get()
    #         print('%s: "%s"' % (field, text))

    # root.bind('<Return>', lambda event: fetch(event))

    root.mainloop()


if __name__ == "__main__":

    try:

        main()

    except Exception as ex:

        print(ex)
