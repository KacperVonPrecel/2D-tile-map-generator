import sys
from PyQt6.QtWidgets import QApplication, QWidget


def guimain(args):
    app = QApplication(args)
    window = QWidget()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guimain(sys.argv)
