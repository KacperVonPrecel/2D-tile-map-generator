class Terrain:
    def __init__(self, name, height, moisture, temperature, colour):
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
