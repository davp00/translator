from translations.manager import get_translation


class Translator:
    def __init__(self, value):
        self.translation = get_translation(value)

    def translate(self, tokens):
        res = ""
        for token in tokens:
            word = self.translation.get(token.word)
            if word:
                context = word.get('context')
                if context:
                    context_translate = context.get(token.value)
                    value = context_translate if context_translate else word.get('literal')
                else:
                    value = word.get('literal')
            else:
                value = token.word

            res += value + " "
        return res