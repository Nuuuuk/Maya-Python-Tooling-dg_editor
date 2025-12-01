"""
create nodes from input expressions
'joint_0: joint'
"""

# for py2
from __future__ import unicode_literals, print_function
import re

class TokenBase(object):
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return "{}<{}>".format(self.__class__.__name__, self.text)

class TokenColon(TokenBase):
    pass

class TokenName(TokenBase):
    pass

class TokenLF(TokenBase):
    pass

class NodeCreateExpExc(Exception):
    pass

# name_match = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')
name_match = re.compile(r'[a-zA-Z0-9_]+')
colon_match = re.compile(r':')
linefeed_match = re.compile(r'(\r\n|\n)+')  # \r\n first
space_match = re.compile(r'[ \t]+')

# process the lex text by grammar
def parser(exp):
    tokens = list(_lex(exp))
    while True:
        if len(tokens) == 0:
            return

        # remove and skip line feed
        if isinstance(tokens[0], TokenLF):
            tokens.pop(0)
            continue

        # correct grammar
        if isinstance(tokens[0], TokenName) and \
                isinstance(tokens[1], TokenColon) and \
                isinstance(tokens[2], TokenName):
            yield tokens[0].text, tokens[2].text # yield current pair
            # remove a group of correct grammar
            tokens = tokens[3:]
            continue

        raise NodeCreateExpExc('syntax error')

# read the text
def _lex(exp):
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

        # match colon
        m = colon_match.match(exp)
        if m is not None:
            token = TokenColon(":")
            exp = exp[1:]
            yield token
            continue

        # match line feed
        m = linefeed_match.match(exp)
        if m is not None:
            token = TokenLF(exp[m.start(): m.end()])
            exp = exp[m.end():]
            yield token
            continue
        raise NodeCreateExpExc('lex error')

if __name__ == "__main__":
    test_exp = ("""\t\r\n
    abc: def
    ghi: jkl""")
    print('test lex')
    print(list(_lex(test_exp)))
    print('test syntax')
    print(list(parser(test_exp)))