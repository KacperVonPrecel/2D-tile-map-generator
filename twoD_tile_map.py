import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise
from terrain import Terrain
from io import BytesIO


def diffrence_val(terrain: Terrain, height: float, moisture: float, temp: float):
    return (
        (height - terrain.height_min) +
        (moisture - terrain.moisture_min) +
        (temp - terrain.temperature_min)
        )


def get_terrain(height: float, moisture: float, temperature: float):
    terrain_list = [
        Terrain("Water", -1.00, -1.00, -1.00, [23, 137, 230]),
        Terrain("Grasslands", -0.20, -0.20, -0.20, [62, 209, 40]),
        Terrain("Forests", -0.10, -0.10, -0.10, [26, 99, 15]),
        Terrain("Mountains", 0.0, 0.0, 0.0, [145, 145, 148]),
        Terrain("Sand", -0.20, -0.25, -0.25, [235, 206, 19]),
        Terrain("Snow", 0.1, 0.1, 0.1, [250, 247, 247])
    ]

    checking_list = []
    diff_list = []
    for terrain in terrain_list:
        if (height >= terrain.height_min
            and moisture >= terrain.moisture_min
                and temperature >= terrain.temperature_min):
            checking_list.append(terrain)

    for terrain in checking_list:
        diff_list.append(diffrence_val(terrain, height, moisture, temperature))

    compare_list = zip(checking_list, diff_list)
    compare_list_sorted = sorted(compare_list, key=lambda x: x[1])
    return compare_list_sorted[0][0]


def create_array(height, width, noise1, noise2, noise3):
    wanted_array = []
    for row in range(height):
        row_table = []
        for column in range(width):
            noise_value = noise1([row / height, column / width])
            noise_value += 0.25 * noise2([row / height, column / width])
            noise_value += 0.125 * noise3([row / height, column / width])
            row_table.append(noise_value)
        wanted_array.append(row_table)
    return wanted_array


class TileMap:
    def __init__(self, height=50, width=50, seed=None):
        self._seed = seed
        self._map_array = np.zeros([height, width, 3], dtype=np.uint8)
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def seed(self):
        return self._seed

    def generate_map(self):
        height_noise1 = PerlinNoise(7, self._seed)
        height_noise2 = PerlinNoise(14, self._seed)
        height_noise3 = PerlinNoise(28, self._seed)

        moisture_noise1 = PerlinNoise(5, self._seed)
        moisture_noise2 = PerlinNoise(10, self._seed)
        moisture_noise3 = PerlinNoise(20, self._seed)

        temperature_noise1 = PerlinNoise(6, self._seed)
        temperature_noise2 = PerlinNoise(12, self._seed)
        temperature_noise3 = PerlinNoise(24, self._seed)

        hg = self._height
        wd = self._width

        height_array = create_array(hg, wd,
                                    height_noise1,
                                    height_noise2,
                                    height_noise3)

        moisture_array = create_array(hg, wd,
                                    moisture_noise1,
                                    moisture_noise2,
                                    moisture_noise3)

        temperature_array = create_array(hg, wd,
                                    temperature_noise1,
                                    temperature_noise2,
                                    temperature_noise3)

        for row in range(len(self._map_array)):
            for column in range(len(self._map_array[row])):
                height = height_array[row][column]
                moisture = moisture_array[row][column]
                temperature = temperature_array[row][column]
                terrain_fill = get_terrain(height, moisture, temperature)
                np.put(self._map_array[row][column], [0, 1, 2], terrain_fill.rgb)

        buffer = BytesIO()
        img = Image.fromarray(self._map_array, mode="RGB")
        img.save(buffer, "PNG")
        return buffer.getvalue()
