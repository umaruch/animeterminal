class Color:
    def __init__(self, id: int, red: int, green: int, blue: int) -> None:
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue

    # Сравнивает похожесть цветов
    def __eq__(self, other):
        if isinstance(other, Color):
            return self.red == other.red and self.green == other.green and self.blue == other.blue
        return NotImplemented
