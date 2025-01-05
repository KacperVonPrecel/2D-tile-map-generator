import sys
from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QIntValidator
from PyQt6.QtCore import Qt
from ui_mapgenerator import Ui_MainWindow

from twoD_tile_map import TileMap


class MapGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupbuttons()
        int_bottom_margin = QIntValidator(1, 9999)
        self.ui.width_box.setValidator(int_bottom_margin)
        self.ui.height_box.setValidator(int_bottom_margin)
        self.ui.seed_box.setValidator(int_bottom_margin)
        self._pix_height = 50
        self._pix_width = 50
        self._current_map = None

    def setupbuttons(self):
        self.ui.generate_map_button.clicked.connect(self.generate_map_img)
        self.ui.actionLoad_Map.triggered.connect(self.load_map)
        self.ui.actionSave_Map.triggered.connect(self.save_map)
        self.ui.scaleslider.sliderReleased.connect(self.scalemap)

    def scalemap(self):
        scalefactor = self.ui.scaleslider.value()
        pixmap = self.ui.map_box.pixmap()
        scaled_pixmap = pixmap.scaled(self._pix_width * scalefactor, self._pix_height * scalefactor, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.map_box.setPixmap(scaled_pixmap)

    def generate_map_img(self):
        self.ui.scaleslider.setSliderPosition(0)
        if self.ui.height_box.text():
            self._pix_height = int(self.ui.height_box.text())
        if self.ui.width_box.text():
            self._pix_width = int(self.ui.width_box.text())
        if self.ui.seed_box.text():
            seed = int(self.ui.seed_box.text())
        else:
            seed = None

        map_to_generate = TileMap(self._pix_height, self._pix_width, seed)
        image_data = map_to_generate.generate_map()
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            pixmap.scaled(pixmap.width(), pixmap.height(), Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.map_box.setPixmap(pixmap)
            self._current_map = self.ui.map_box.pixmap().toImage()

    def save_map(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save Map')
        map_to_save = self.ui.map_box.pixmap()
        map_to_save.save(name)

    def load_map(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Load Map')
        map_to_load = QPixmap()
        map_to_load.load(name)
        map_to_load.scaled(map_to_load.width(), map_to_load.height(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.map_box.setPixmap(map_to_load)


def guimain(args):
    app = QApplication(args)
    window = MapGeneratorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guimain(sys.argv)
