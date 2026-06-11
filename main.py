import tkinter as tk

from gui.validation_gui import ValidationGUI


def main():

    root = tk.Tk()

    app = ValidationGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()