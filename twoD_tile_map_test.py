from twoD_tile_map import TileMap
from twoD_tile_map import get_terrain, difference_val, create_array
from perlin_noise import PerlinNoise
import pytest
from terrain import Terrain


def test_initialization_typical():
    tilemap = TileMap(10, 10, 10)
    assert tilemap.height == 10
    assert tilemap.width == 10
    assert tilemap.seed == 10
    for row in range(10):
        for column in range(10):
            for byte in range(3):
                assert tilemap._map_array[row][column][byte] == 0


def test_initialization_default():
    tilemap = TileMap()
    assert tilemap.height == 50
    assert tilemap.width == 50
    assert tilemap._seed == None
    for row in range(50):
        for column in range(50):
            for byte in range(3):
                assert tilemap._map_array[row][column][byte] == 0


def test_initialization_wrong_seed_type():
    with pytest.raises(TypeError):
        tilemap1 = TileMap(10, 10, "aaa")


def test_initialization_wrong_seed_value():
    with pytest.raises(ValueError):
        tilemap1 = TileMap(10, 10, -10)


def test_initialization_wrong_height_or_width_type():
    with pytest.raises(TypeError):
        tilemap1 = TileMap("ab", "cd")


def test_initialization_wrong_height_or_width_value():
    with pytest.raises(TypeError):
        tilemap1 = TileMap(-10, 10)
        tilemap2 = TileMap(10, -10)
        tilemap3 = TileMap(-10, -10)


def test_get_terrain_one_candidate():
    terrain = get_terrain(-1.00, -1.00, -1.00)
    assert terrain.name == "Water"


def test_get_terrain_more_candidates():
    terrain = get_terrain(0.35, 0.35, 0.90)
    assert terrain.name == "Snow"


def test_difference_value():
    terrain = Terrain("Grasslands", -0.20, -0.20, -0.20, [62, 209, 40])
    height = 0.25
    moisture = 0.11
    temperature = -0.20

    assert difference_val(terrain, height, moisture, temperature) == 0.76


def test_create_array():
    noise1 = PerlinNoise(2)
    noise2 = PerlinNoise(4)
    noise3 = PerlinNoise(6)
    height = 50
    width = 50
    test_array = create_array(height, width, noise1, noise2, noise3)
    for row in range(width):
        for column in range(height):
            assert test_array[row][column] is not None
