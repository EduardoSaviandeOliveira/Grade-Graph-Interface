from PyQt6.QtWidgets import *

class WindowLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")


        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.set

    def the_button_was_clicked(self):
        print("Clicked!")
    