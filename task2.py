# 2. Створити context manager який буде фарбувати колір виведеного тексту

class Colors:
    COLORS_DICT = {'GREY': '\033[90m', 'RED': '\033[91m', 'GREEN': '\033[92m', 'YELLOW': '\033[93m',
                   'BLUE': '\033[94m', 'PINK': '\033[95m', 'TURQUOISE': '\033[96'}

    def __init__(self, color):
        if isinstance(color, str):
            self.color = color.upper()
        try:
            self.color_number = Colors.COLORS_DICT[self.color]
        except:
            self.color = 'default'
            self.color_number = '\033[90m'

    def __enter__(self):
        print(self.color_number)
        return self.color

    def __exit__(self, *args):
        return self


with Colors('red') as col:
    print(f'printed in {col.lower()}')
