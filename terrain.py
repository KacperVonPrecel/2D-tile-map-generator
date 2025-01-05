class Terrain:
    """
    A class representing a certain type of terrain.

    Attributes:
        name: The name of the terrain
        height_min: The minimal height value required for that terrain to spawn
        moisture_min: The minimal moisture value required for that terrain to spawn
        temperature_min: The minimal temperature required for that terrain to spawn
        colour_RGB: a list containing a colour of the terrain written in RGB

    """

    def __init__(
            self,
            name: str,
            height: float,
            moisture: float,
            temperature: float,
            colour: list[int, int, int]
            ):
        self._name = name
        self._height_min = height
        self._moisture_min = moisture
        self._temperature_min = temperature
        self._colour_RGB = colour

    @property
    def name(self):
        return self._name

    @property
    def height_min(self):
        return self._height_min

    @property
    def moisture_min(self):
        return self._moisture_min

    @property
    def temperature_min(self):
        return self._temperature_min

    @property
    def rgb(self):
        return self._colour_RGB
