from terrain import Terrain


def test_create_typical():
    terrain = Terrain("Dirt", 0.1, 0.5, 0.5, [255, 0, 0])
    assert terrain.name == "Dirt"
    assert terrain.height_min == 0.1
    assert terrain.moisture_min == 0.5
    assert terrain.temperature_min == 0.5
    assert terrain.colour_rgb == [255, 0, 0]
