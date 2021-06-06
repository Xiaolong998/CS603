# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:02:22 2021

@author: xiaol
"""


import calculator_lexer as cl
import calculator_parser as cp

lex = cl.get_lexer()
parser = cp.get_parser()

end_condition = 1

while end_condition != 0:
    print("0: stop program \n1: calculate an expression")
    v = input("Enter your choice: ")
    if int(v) == 0:
        break
    else:
        ip = input("Enter your expression: ")
        
        result = parser.parse(lex.lex(ip)).evaluate()
        print('='+str(result))
    
    
