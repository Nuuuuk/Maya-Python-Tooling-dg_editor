"""
generate names eg ['box_0_joint', 'box_2_joint', 'box_3_joint']
"""

# for py2
from __future__ import unicode_literals, print_function
import re

class TokenBase(object):
    def __init__(self, text):
        self.text = textif __name__ == "__main__":

def _lex(exp):
    """
    :param exp: abc_{value_name} or abc_{value_name} or abc_{value_name}_def
    :return:
    """

        raise GenNameExpExc('lex error')

    test_exp = ("box_{name_id}_joint")
    print('test lex')
    print(list(_lex(test_exp)))