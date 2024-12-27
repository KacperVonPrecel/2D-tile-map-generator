from twoD_tile_map import TileMap


def test_create_blank_map():
    tilemap = TileMap(10, 10, 1)
    assert tilemap._seed == 1
    for row in range(10):
        for column in range(10):
            for byte in range(3):
                assert tilemap._map_array[row][column][byte] == 0
