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

    def literal_verb(self, item):
        tokens.append(Token('', item))

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

    def to_be_f(self, item):
        tokens.append(Token('to_be_f', item))

    def to_be_s(self, item):
        tokens.append(Token('to_be_s', item))

    def to_be_t(self, item):
        tokens.append(Token('to_be_t', item))

    def pa_to_be_f_t(self, item):
        tokens.append(Token('pa_to_be_f_t', item))

    def pa_to_be(self, item):
        tokens.append(Token('pa_to_be', item))

    def to_be_plural(self, item):
        tokens.append(Token('to_be_plural', item))

    def preposition(self, item):
        tokens.append(Token('', item))

    def adv_freq(self, item):
        tokens.append(Token('', item))