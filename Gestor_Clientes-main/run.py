from tkinter import Menu
import ui
import sys
from gestor.menu import *

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        Menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()
