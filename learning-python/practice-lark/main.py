from lark import Lark

with open('grammar.lark') as f:
    grammar = f.read()

parser = Lark(grammar=grammar, start='query', lexer='basic')

text = 'Hell* World Testing'

print(parser.parse(text))
