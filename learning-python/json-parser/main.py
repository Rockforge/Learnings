import sys
from src.transformer import MyTransformer, TreeToJson
from lark import Lark


json_grammar = r"""
    ?value: dict
        | list
        | string
        | SIGNED_NUMBER -> number
        | "true" -> true
        | "false" -> false
        | "null" -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
"""

text = '{"key": ["item0", "item1", 3.14, true]}'

json_parser = Lark(json_grammar, start='value', lexer='standard')

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        tree = json_parser.parse(f.read())
        print(TreeToJson().transform(tree))
