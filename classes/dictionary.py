class Languaje:

    def __init__(self):
        self.words = {}
        self.grammar = ""

    def parse_key(self, key):
        cad = ""
        for element in self.words.get(key):
            cad += '\"{}\" |'.format(element)

        cad = cad[:len(cad) - 1]
        return cad

    @staticmethod
    def parse_obj(elements):
        cad = ""
        for element in elements:
            cad += '\"{}\" |'.format(element)
        cad = cad[:len(cad) - 1]
        return cad

    def get_grammar(self):
        return self.grammar