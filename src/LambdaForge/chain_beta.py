from lambda_terms import Abstraction, FunctionApplication

def chain_beta_reduce(abstraction: Abstraction, args: list):
    """
    Applies a series of arguments to an abstraction using beta reduction.

    This function takes an abstraction and a list of arguments, and
    applies each argument to the abstraction in sequence, performing
    beta reduction at each step. The final result is returned.

    Parameters:
        abstraction (Abstraction): The lambda abstraction to be reduced.
        args (list): A list of arguments to be applied to the abstraction.

    Returns:
        The final result after applying all arguments to the abstraction.
    """
    num_args = len(args)
    if num_args == 0:
        print(f"No arguments provided for beta reduction. Returning {abstraction}")
        return abstraction
    else:
        print(f"Starting beta reduction with {num_args} arguments.")
        print(f"Initial abstraction: {abstraction}")
        abstract =  abstraction
        for i in range(num_args):
            print(f"Applying argument {i+1}: {args[i]}")
            # Apply the argument to the abstraction
            print(f"Before beta reduction: {abstract}")
            print(type(abstract))
            print(type(args[i]))
            abstract = FunctionApplication(abstract, args[i]).beta_reduce()
            print(f"After beta reduction: {abstract}")
        print(f"Final result after beta reduction: {abstract}")
        
        
def func_chain_beta_reduce(expr: FunctionApplication):
    args = expr.arg
    abstraction = expr.func
    num_args = len(args)
    if num_args == 0:
        print(f"No arguments provided for beta reduction. Returning {abstraction}")
        return abstraction
    else:
        print(f"Starting beta reduction with {num_args} arguments.")
        print(f"Initial abstraction: {abstraction}")
        abstract =  abstraction
        for i in range(num_args):
            print(f"Applying argument {i+1}: {args[i]}")
            # Apply the argument to the abstraction
            print(f"Before beta reduction: {abstract}")
            abstract = FunctionApplication(abstract, args[i]).beta_reduce()
            print(f"After beta reduction: {abstract}")
        print(f"Final result after beta reduction: {abstract}")
        return abstract