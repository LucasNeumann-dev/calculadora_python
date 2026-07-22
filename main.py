import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    # label1 = QLabel('Texto apenas para demonstração')
    # label1.setStyleSheet('font-size: 50px; ')
    # window.addWidgetToVLayout(label1)

    # define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # define o display da calculadora
    display = Display()
    window.addWidgetToVLayout(display)

    window.show()
    app.exec()
