from twoD_tile_map import TileMap
from twoD_tile_map import get_terrain


def test_create_blank_map():
    tilemap = TileMap(10, 10, 1)
    assert tilemap._seed == 1
    for row in range(10):
        for column in range(10):
            for byte in range(3):
                assert tilemap._map_array[row][column][byte] == 0


def test_get_terrain_one_candidate():
    terrain = get_terrain(0.40, 0.40, 0.55)
    assert terrain.name == "Grasslands"


def test_get_terrain_more_candidates():
    terrain = get_terrain(0.35, 0.35, 0.90)
    assert terrain.name == "Dessert"
