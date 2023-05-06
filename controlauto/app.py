import tkinter as tk
from view.user_view import UserView


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
