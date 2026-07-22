from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QWidget


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def configStyle(self):
        self.style =
