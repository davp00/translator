from translations.manager import get_translation


class Translator:
    def __init__(self, value):
        self.translation = get_translation(value)
        print(self.translation)

    def translate(self, tokens):
        pass