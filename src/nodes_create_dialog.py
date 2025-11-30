"""
Generate names variations based on tokens
from: 'box_{id}', 'joint'
to: ['box_0_joint', 'box_2_joint', 'box_3_joint']
"""

# for py2
from __future__ import unicode_literals, print_function
import re

class TokenBase(object):
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return "{}<{}>".format(self.__class__.__name__, self.text)
class TokenName(TokenBase):
    pass
class TokenValue(TokenBase):
    pass
class CreateDialogParserExc(Exception):
    pass
# Compiled Regex patterns
name_match = re.compile(r'[a-zA-Z0-9_]+')
value_match = re.compile(r'\{([a-zA-Z0-9_]+)\}')
space_match = re.compile(r'[ \t]+')

def _lex(exp):
    """
    :param exp: abc_{value_name} or abc_{value_name} or abc_{value_name}_def
    :return:
    """
    while True:
        if len(exp) == 0:
            return

        # skip space
        m = space_match.match(exp)
        if m is not None:
            exp = exp[m.end():]

        # match name
        m = name_match.match(exp)
        if m is not None:
            token = TokenName(exp[m.start(): m.end()])
            exp = exp[m.end():]
            yield token
            continue

        # match value
        m = value_match.match(exp)
        if m is not None:
            token = TokenValue(m.group(1))# Extract content inside {}
            exp = exp[m.end():]
            yield token
            continue

        raise CreateDialogParserExc('Lex error: Unexpected character')

def parse(exp, values):
    """
    :param exp: abc_{value_name} or abc_{value_name} or abc_{value_name}_def
    :param values: List of dicts e.g. [{"id": 0}, {"id": 1}]
    """
    tokens = list(_lex(exp))

    for kv in values:
        name = ''
        for t in tokens:
            if isinstance(t, TokenName):
                name += t.text
            else:
                v = kv.get(t.text)
                if v is None:
                    raise CreateDialogParserExc("Key not found")
                name += str(v)
        yield name

if __name__ == "__main__":
    test_exp = ("box_{name_id}_joint")
    print('test lex')
    print(list(_lex(test_exp)))
    print('test parse')
    print(list(parse(test_exp,[
        {"name_id": 0},
        {"name_id": 2},
        {"name_id": 3},
    ])))