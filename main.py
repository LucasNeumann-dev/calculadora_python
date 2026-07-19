import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()

    central_widget = QWidget()
    vertical_layout = QVBoxLayout()
    central_widget.setLayout(vertical_layout)

    label1 = QLabel('Texto apenas para demonstração')
    vertical_layout.addWidget(label1)

    window.setCentralWidget(central_widget)
    window.show()

    app.exec()
