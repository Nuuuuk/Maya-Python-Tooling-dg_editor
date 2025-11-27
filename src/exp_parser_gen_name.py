"""
generate names eg ['box_0_joint', 'box_2_joint', 'box_3_joint']
"""

# for py2
from __future__ import unicode_literals, print_function
import re

class TokenBase(object):
    def __init__(self, text):
        self.text = textif __name__ == "__main__":
class TokenName(TokenBase):
    pass
class TokenValue(TokenBase):
    pass
class GenNameExpExc(Exception):
    pass

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
            token = TokenValue(m.group(1))
            exp = exp[m.end():]
            yield token
            continue

        raise GenNameExpExc('lex error')

    test_exp = ("box_{name_id}_joint")
    print('test lex')
    print(list(_lex(test_exp)))