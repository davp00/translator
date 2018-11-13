from dictionaries.manager import get_languaje
from lark import Lark


class Parser:
    def __init__(self, languaje):
        self.languaje = get_languaje(languaje)
        self.p = Lark(self.languaje.get_grammar(), start='sentence', ambiguity='explicit')

    def parse_text(self, text):
        tree = self.p.parse(text)
        print(tree)