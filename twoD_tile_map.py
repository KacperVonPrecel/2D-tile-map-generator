import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise
from terrain import Terrain


def get_terrain(height, moisture, temperature):
    terrain_list = [
        Terrain("Grasslands", 0.35, 0.35, 0.60, [62, 209, 40]),
        Terrain("Desserts", 0.30, 0.00, 0.90, [235, 206, 19]),
        Terrain("Sea", 0.20, 1.00, 0.40, [19, 141, 235]),
        Terrain("Ocean", 0.10, 1.00, 0.35, [19, 48, 235]),
        Terrain("Mountains", 0.75, 0.60, 0.20, [145, 145, 148]),
        Terrain("Woodlands", 0.45, 0.50, 0.50, [26, 99, 15])
    ]


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
