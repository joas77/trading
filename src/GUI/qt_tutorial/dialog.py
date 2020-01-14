import sys
from PySide2.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QVBoxLayout)

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        # create widgets
        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print("Hello {}".format(self.edit.text()))


if __name__=="__main__":
    # Create the Qt Application
    app = QApplication([])
    # Create and show the form
    form = Form()
    form.show()
    # run the main Qt loop
    sys.exit(app.exec_())