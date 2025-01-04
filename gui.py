import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from ui_mapgenerator import Ui_MainWindow

from twoD_tile_map import TileMap


class MapGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupbuttons()

    def setupbuttons(self):
        self.ui.generate_map_button.clicked.connect(self.generate_map_img)
        self.ui.actionLoad.triggered.connect(self.load_map)
        self.ui.actionSave.triggered.connect(self.save_map)

    def generate_map_img(self):
        height = int(self.ui.height_box.text())
        width = int(self.ui.width_box.text())
        seed = int(self.ui.seed_box.text())

        map_to_generate = TileMap(height, width, seed)
        image_data = map_to_generate.generate_map()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.map_box.setPixmap(pixmap)
            self.ui.map_box.adjustSize()

    def save_map(self):
        pass

    def load_map(self):
        pass


def guimain(args):
    app = QApplication(args)
    window = MapGeneratorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guimain(sys.argv)
