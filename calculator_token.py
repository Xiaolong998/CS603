# -*- coding: utf-8 -*-
"""
This script defines tokens used in the calculator, aka abstrct syntax tree

Created on Thu Jun  3 20:40:47 2021

@author: xiaol
"""

from rply.token import BaseBox

class Num(BaseBox):
    def __init__(self, val):
        if type(val) is not int:
            val = int(val)
        self.value = val
    
    def evaluate(self):
        return self.value
    

class BinaryOperation(BaseBox):
    def __init__(self,l,r):
        self.left = l
        self.right = r
        
        
class Add(BinaryOperation):
    """
    Addition operation
    """
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    

class Minus(BinaryOperation):
    """
    Minus Operation
    """
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()
    

class Times(BinaryOperation):
    """
    Multiplication Operation
    """
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Divide(BinaryOperation):
    """
    Division Operation
    """
    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

class Exponential(BinaryOperation):
    """
    Exponential Operation
    """
    def evaluate(self):
        return self.left.evaluate() ** self.right.evaluate()
    
