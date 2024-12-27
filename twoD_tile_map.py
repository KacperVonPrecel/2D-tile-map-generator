import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise


class TileMap:
    def __init__(self, height, width, seed):
        self._seed = seed
        self._map_array = np.zeros([height, width, 3], dtype=np.uint8)
        self._height = height
        self._width = width

    def generate_map(self):
        height_noise = PerlinNoise(10, self._seed)
        moisture_noise = PerlinNoise(4, self._seed)
        temperature_noise = PerlinNoise(3, self._seed)

        hg = self._height
        wd = self._width

        height_array = [
            [height_noise(row / hg, column / wd) for column in range(wd)]
            for row in range(hg)
            ]

        moisture_array = [
            [moisture_noise(row / hg, column / wd) for column in range(wd)]
            for row in range(hg)
            ]

        temperature_array = [
            [temperature_noise(row / hg, column / wd) for column in range(wd)]
            for row in range(hg)
            ]

    def load_map(self, path_from):
        pass

    def write_map(self, path_to):
        pass

    def __str__(self):
        pass
