import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create the Qt application
app = QApplication([])
# Create a button
button = QPushButton("click me")
# Connect the button to the function
button.clicked.connect(say_hello)
# Show the button
button.show()
# Run the main Qt loop
app.exec_()
