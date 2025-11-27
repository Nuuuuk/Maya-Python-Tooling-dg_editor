"""
create nodes from input text
"""

# for py2
from __future__ import unicode_literals, print_function
import re

class TokenBase(object):
    def __init__(self, text):
        self.text = text

class TokenColon(TokenBase):
    pass

class TokenName(TokenBase):
    pass

class TokenLF(TokenBase):
    pass

class ExpExc(Exception):
    pass

class Exp(object):
    # name_match = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')
    name_match = re.compile(r'[a-zA-Z0-9]+')
    colon_match = re.compile(r':')
    linefeed_match = re.compile(r'(\r\n|\n)+')  # \r\n first
    space_match = re.compile(r'[ \t]+')

    def __init__(self, exp):
        self.exp = exp

    # process the lex text by grammar
    def __iter__(self):
        tokens = list(self._lex())
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

            raise ExpExc('syntax error')

    # read the text
    def _lex(self):
        exp = self.exp
        while True:
            if len(exp) == 0:
                return

            # skip space
            m = self.space_match.match(exp)
            if m is not None:
                exp = exp[m.end():]

            # match name
            m = self.name_match.match(exp)
            if m is not None:
                token = TokenName(exp[m.start(): m.end()])
                exp = exp[m.end():]
                yield token
                continue

            # match colon
            m = self.colon_match.match(exp)
            if m is not None:
                token = TokenColon(":")
                exp = exp[1:]
                yield token
                continue

            # match line feed
            m = self.linefeed_match.match(exp)
            if m is not None:
                token = TokenLF(exp[m.start(): m.end()])
                exp = exp[m.end():]
                yield token
                continue
            raise ExpExc('lex error')

if __name__ == "__main__":
    test_exp = ("""\t\r\n
    abc: def
    ghi: jkl""")
    print('test lex')
    print(list(Exp(test_exp)._lex()))
    print('test syntax')
    print(list(Exp(test_exp)))