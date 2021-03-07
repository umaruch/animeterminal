from PIL import Image


class Art:
    def __init__(self, image_path: str) -> None:
        self.image = Image.open(image_path)

    def get_rgb_pixel(self, x: int, y: int):
        data = self.image.getpixel((x, y))
        return data

    # возвращает некоторую еденицу масштабирования изображения к консоли
    def analyze_image(self, console_width: int, console_height: int) -> int:
        if console_width > console_height:
            console_size = console_height
        else:
            console_size = console_width

        if self.image.width > self.image.height:
            image_size = self.image.height
        else:
            image_size = self.image.width

        return image_size // console_size, console_size
