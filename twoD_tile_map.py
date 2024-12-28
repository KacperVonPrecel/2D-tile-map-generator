import numpy as np
from PIL import Image
from perlin_noise import PerlinNoise
from terrain import Terrain


def diffrence_val(terrain: Terrain, height: float, moisture: float, temp: float):
    return (
        (height - terrain.height_min) +
        (moisture - terrain.moisture_min) +
        (temp - terrain.temperature_min)
        )


def get_terrain(height: float, moisture: float, temperature: float):
    terrain_list = [
        Terrain("Grasslands", 0.00, 0.00, 0.10, [62, 209, 40]),
        Terrain("Dessert", 0.00, -1.00, 0.30, [235, 206, 19]),
        Terrain("Ocean", -1.00, -1.00, -1.00, [19, 48, 235]),
        Terrain("Mountains", 0.35, -1.00, -1.00, [145, 145, 148]),
        Terrain("Forest", 0.10, 0.10, 0.15, [26, 99, 15])
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


class TileMap:
    def __init__(self, height, width, seed=None):
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
            [height_noise([row / hg, column / wd]) for column in range(wd)]
            for row in range(hg)
            ]

        moisture_array = [
            [moisture_noise([row / hg, column / wd]) for column in range(wd)]
            for row in range(hg)
            ]

        temperature_array = [
            [temperature_noise([row / hg, column / wd]) for column in range(wd)]
            for row in range(hg)
            ]

        for row in range(len(self._map_array)):
            for column in range(len(self._map_array[row])):
                height = height_array[row][column]
                moisture = moisture_array[row][column]
                temperature = temperature_array[row][column]
                terrain_fill = get_terrain(height, moisture, temperature)
                np.put(self._map_array[row][column], [0, 1, 2], terrain_fill.rgb)

    def load_map(self, path_from):
        pass

    def write_map(self, path_to):
        pass

    def save(self):
        img = Image.fromarray(self._map_array)
        img.save("test.png")


def main():
    test_map = TileMap(100, 100, 1234)
    test_map.generate_map()
    test_map.save()


if __name__ == "__main__":
    main()
