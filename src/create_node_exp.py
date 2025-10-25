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

class Exp(object):
    # name_match = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')
    name_match = re.compile(r'[a-zA-Z0-9]+')
    colon_match = re.compile(r':')
    space_match = re.compile(r' +')

    def __init__(self, exp):
        self.exp = exp

    def __iter__(self):
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

if __name__ == "__main__":
    print(list(Exp("abc: def")))