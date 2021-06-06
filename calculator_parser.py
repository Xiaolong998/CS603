# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 23:06:39 2021

@author: xiaol
"""

from rply import ParserGenerator
import calculator_token as ct
import pdb

def get_parser():

    par_gen = ParserGenerator(
        # type of tokens used in the calculator
        ['num','add','minus','times','division','exponential','LParen','RParen',
         "Ltriple","Ldouble"
         ],
        precedence=[
            
            ('left',['add','minus']),
            ('left',['times','division']),
            ('left',['exponential'])
            ]
        )
    
    @par_gen.production('expression : num')
    def expression_num(tk):
        """
        number
        """
        return ct.Num(tk[0].getstr())
    
    @par_gen.production('expression : LParen expression RParen')
    def parentheses(tk):
        return tk[1]
    
    @par_gen.production('expression : Ldouble expression RParen')
    def double(tk):
        num = 2*(tk[1].evaluate())
        return ct.Num(num)
        
    @par_gen.production('expression : Ltriple expression RParen')
    def triple(tk):
        num = 3*(tk[1].evaluate())
        return ct.Num(num)
    
    
    
    @par_gen.production("expression : expression add expression")
    @par_gen.production("expression : expression minus expression")
    @par_gen.production("expression : expression times expression")
    @par_gen.production("expression : expression division expression")
    @par_gen.production("expression : expression exponential expression")
    def expression_binary_operation(tk):
        """
        Backus-Naur form:
        expr : term add|minus term 
        term: factor times|divide factor
        factor: factor exponential factor | number
         "(" <expression> ")"
        """
        token_type = tk[1].gettokentype()
        l = tk[0]
        r = tk[2]
        
        if token_type == 'add':
            result = ct.Add(l, r)
        
        elif token_type == 'minus':
            result = ct.Minus(l, r)
    
        elif token_type == 'times':
            result = ct.Times(l, r)
            
        elif token_type == 'division':
            result = ct.Divide(l, r)
        
        elif token_type == 'exponential':
            result = ct.Exponential(l, r)
        
        else:
            raise Exception("Input cannot be calculated")
        
        return result
    
    parser = par_gen.build()
            
    return parser            
        
