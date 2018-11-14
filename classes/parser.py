from dictionaries.manager import get_languaje
from lark import Lark, Transformer, InlineTransformer
from classes.token import Token


tokens = []


class Parser:
    def __init__(self, languaje):
        self.languaje = get_languaje(languaje)
        self.p = Lark(self.languaje.get_grammar(), start='sentence', ambiguity='explicit')

    def parse_text(self, text):
        tree = self.p.parse(text)
        tree_parser = TreeParser()
        return tree_parser.transform(tree).data


class TreeParser(InlineTransformer):

    def article(self, item):
        tokens.append(Token('article', item))

    def verb(self, item):
        tokens.append(Token('verb', item))

    def past_verb(self, item):
        tokens.append(Token('past_verb', item))

    def tp_verb(self, item):
        tokens.append(Token('tp_verb', item))

    def pro_f_s(self, item):
        tokens.append(Token('pro_f_s', item))

    def pro_third(self, item):
        tokens.append(Token('pro_third', item))

    def adj(self, item):
        tokens.append(Token('adj', item))

    def connector(self, item):
        tokens.append(Token('connector', item))

    def noun(self, item):
        tokens.append(Token('noun', item))

    def popper_noun(self, item):
        tokens.append(Token('popper_noun', item))

    def object(self, item):
        tokens.append(Token('object', item))

    def sym_interrogative(self, item):
        tokens.append(Token('sym_interrogative', item))

    def pro_f(self, item):
        tokens.append(Token('pro_f', item))

    def pro_s(self, item):
        tokens.append(Token('pro_s', item))

    def pro_plural(self, item):
        tokens.append(Token('pro_plural', item))