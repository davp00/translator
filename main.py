from classes.parser import Parser, tokens
from classes.translator import Translator

parser = Parser('en')

sentence = parser.parse_text('he talks')

sentence = sentence.replace('_', ' ')
print(sentence)

translator = Translator('en_es')
result = translator.translate(tokens)

print(result)