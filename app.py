"""
Initializes and runs the Wikipedia Reader application using PyQt6 for the GUI.
"""


from PyQt6 import QtWidgets
import sys
import gui


# Run the program.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = gui.UiPage()
    ui.setup_ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
