from lambda_terms import FunctionApplication, Abstraction, Var

def tree_form(object):
    # Create a tree form of the object by recursively traversing its structure and returning all 
    # the permutations of the object
    permutations = []
    if isinstance(object, FunctionApplication):
        permutations.append(object)
        permutations.append(tree_form(object.func))
        permutations.append(tree_form(object.arg))
    elif isinstance(object, Abstraction):
        permutations.append(object)
        permutations.append(tree_form(object.body))
    elif isinstance(object, Var):
        permutations.append(object)
    elif isinstance(object, Number):
        permutations.append(object)
    else:
        raise ValueError("Unsupported object type for tree form.")
    return permutations