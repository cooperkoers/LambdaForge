from lambda_terms import *
from tree_form import *
import random

class Recombinator:
    def __init__(self, exprs: list, method='blind'):
        """Recombines expressions into a new expression."""
        if len(exprs) < 2:
            raise ValueError("At least two expressions are required for recombination.")
        self.expr = exprs  # The expression to be recombined
        self.method = method

    def __repr__(self):
        return f"Recombinator({self.expr}, {self.method})"
    
    def __str__(self):
        return f"Expressions to be recombined: {self.expr} using method: {self.method}"
    
    def find_motifs(self):
        """Finds motifs in the expressions to be recombined."""
        # Placeholder for motif finding logic
        
        # This could involve analyzing the structure of the expressions
    
    def recombine(self):
        """Recombines the expressions based on the specified method."""
        if self.method == 'blind':
            # Blind recombination: simply concatenate the expressions
            return FunctionApplication(self.expr[0], self.expr[1])
        elif self.method == 'blind_recombination':
            # Blind recombination: create a new expression that combines the first two at random nodes
            tree1 = tree_form(self.expr[0])
            tree2 = tree_form(self.expr[1])
            main_tree = tree1 + tree2

            # pick random nodes from the trees and combine them using function application
            # pick random abstraction
            main_abstr = [x for x in main_tree if isinstance(x, Abstraction)]
            random_abstr = random.choice(main_abstr)
            # pick random argument out of the two trees
            main_arg = random.choice([x for x in main_tree if not isinstance(x, list)] or not isinstance(x, FunctionApplication))

            # 
            #main_arg = random.choice(main_tree)
            print(f"Ranomly selected abstraction: {random_abstr}")
            print(f"Randomly selected argument: {main_arg}")
            print(f"Type of abstraction: {type(random_abstr)}")
            print(f"Type of argument: {type(main_arg)}")

            return FunctionApplication(random_abstr, main_arg)
            
        elif self.method == 'mimic':
            # Mimic recombination: create a new expression that mimics the structure of the first
            # Placeholder for mimic recombination logic
            pass
            
