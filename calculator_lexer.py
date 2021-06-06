# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:30:22 2021

@author: xiaol
"""


from rply import LexerGenerator

def get_lexer():
    # specifying parsing rules
    lex_gen = LexerGenerator()
    
    # tokens defined
    lex_gen.add('num', r'\d+')
    lex_gen.add('add', r'\+')
    lex_gen.add('minus', r'-')
    lex_gen.add('times', r'\*')
    lex_gen.add('division', r'/')
    lex_gen.add('exponential',r'\^')
    lex_gen.add('LParen',r'\(')
    lex_gen.add('RParen',r'\)')
    lex_gen.add('Ldouble',r'double\(')
    lex_gen.add('Ltriple',r'triple\(')
    
    lex_gen.ignore(r'\s+')
    lex_gen.ignore(r'\Z')
    
    lex = lex_gen.build()
    return lex