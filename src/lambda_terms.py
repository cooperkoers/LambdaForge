class Var:
    """
    Represents a variable in lambda calculus.
    
    A variable is a named entity that can be bound in an abstraction or
    used as an argument in a function application. It is immutable and
    can be substituted with another expression.

    Attributes:
        name (str): The name of the variable.

    Methods:
        __repr__(): Returns a string representation of the variable.
        __str__(): Returns the name of the variable.
        substitute(var_name, replacement): Replaces occurrences of var_name with replacement.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"

    def __str__(self):
        return self.name

    def substitute(self, var_name, replacement):
        """Replaces occurrences of var_name with replacement."""
        return replacement if self.name == var_name else self


class Abstraction:
    """
    Represents a lambda abstraction (function definition).

    An abstraction binds a variable to an expression (the body) and can
    be applied to an argument. It is immutable and can be substituted
    with another expression.

    Attributes:
        var (Var): The variable being bound in the abstraction.
        body (Expression): The body of the abstraction (another expression).

    Methods:
        __repr__(): Returns a string representation of the abstraction.
        __str__(): Returns the lambda notation for the abstraction.
        substitute(var_name, replacement): Replaces occurrences of var_name with replacement in the body.
    """
    def __init__(self, var, body):
        self.var = var  # A Var instance representing the bound variable
        self.body = body  # The body of the abstraction (another expression)

    def __repr__(self):
        return f"Abstraction({self.var}, {self.body})"

    def __str__(self):
        return f"λ{self.var}.{self.body}"

    def substitute(self, var_name, replacement):
        """Substitutes var_name with replacement in the body, avoiding variable capture."""
        if self.var.name == var_name:
            return self  # No substitution occurs if the variable is bound
        return Abstraction(self.var, self.body.substitute(var_name, replacement))


class FunctionApplication:
    """
    Represents the application of a function to an argument.
    A function application consists of a function (which can be an
    abstraction or another application) and an argument (which can be
    a variable or another expression).

    Attributes:
        func (Expression): The function being applied (could be an abstraction or another application).
        arg (Expression): The argument being passed to the function.

    Methods:
        __repr__(): Returns a string representation of the function application.
        __str__(): Returns the application notation for the function and argument.
        substitute(var_name, replacement): Replaces occurrences of var_name with replacement in both func and arg.
        beta_reduce(): Performs a single step of beta reduction if applicable.
    """
    def __init__(self, func, arg):
        self.func = func  # A function (lambda abstraction or application)
        self.arg = arg  # The argument being applied

    def __repr__(self):
        return f"FunctionApplication({self.func}, {self.arg})"

    def __str__(self):
        return f"(({self.func}) ({self.arg}))"

    def substitute(self, var_name, replacement):
        """Substitutes var_name with replacement in both the function and argument."""
        return FunctionApplication(
            self.func.substitute(var_name, replacement),  # Substitute in function
            self.arg.substitute(var_name, replacement)    # Substitute in argument
        )

    def beta_reduce(self):
        """Performs a single step of beta reduction."""
        if isinstance(self.func, Abstraction):
            print(f"Beta reducing: {self}")
            print(f"Substituting {self.func.var.name} with {self.arg}")
            return self.func.body.substitute(self.func.var.name, self.arg)
        else:
            print(f"Cannot beta reduce: {self}")
            return self
            #raise ValueError("Cannot beta-reduce a non-abstraction function.")

    
class Number:
    """
    Represents a Church numeral in lambda calculus.
    
    A Church numeral is a higher-order representation of natural numbers
    using lambda calculus. It is defined as a function that takes two
    arguments: a successor function and a base case (zero).

    Attributes:
        n (int): The natural number represented by the Church numeral.

    Methods:
        __repr__(): Returns a string representation of the Church numeral.
        __str__(): Returns the Church numeral in lambda notation.
    """
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Church numerals cannot represent negative numbers.")
        self.n = n
        self.church_n = self.to_church()  # Convert the integer to a Church numeral
        # recursively add function calls
        # ex of n=3: λf.λx.x(f(f(x)))
        

    def __repr__(self):
        return f"Number({self.n})"

    def __str__(self):
        return f"{self.church_n}"
    def to_church(self):
        """Converts the integer to a Church numeral."""
        if self.n == 0:
            return Abstraction(Var("f"), Abstraction(Var("x"), Var("x")))
        # For n > 0, create a Church numeral by applying the successor function
        # recursively n times to the base case (zero)
        # Example for n=3: λf.λx.x(f(f(x)))

        body = Var("x")  
        for _ in range(self.n):  
            body = FunctionApplication(Var("f"), body)  # Apply f repeatedly
        
        return Abstraction(Var("f"), Abstraction(Var("x"), body))