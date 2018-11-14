from classes.parser import Parser, tokens
from classes.translator import Translator

parser = Parser('en')

sentence = parser.parse_text('i talked')

sentence = sentence.replace('_', ' ')
print(sentence)

for token in tokens:
    print("{} - {}".format(token.word, token.value))

translator = Translator('en_es')