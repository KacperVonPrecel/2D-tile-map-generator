import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise


class TileMap:
    def __init__(self, height, width, seed):
        self._seed = seed
        self._map_array = np.zeros([height, width, 3], dtype=np.uint8)

    def generate_map(self):
        height_noise_map = PerlinNoise(10, self._seed)
        moisture_noise_map = PerlinNoise(4, self._seed)
        temperature_noise_map = PerlinNoise(3, self._seed)

    def load_map(self, path_from):
        pass

    def write_map(self, path_to):
        pass

    def __str__(self):
        pass
