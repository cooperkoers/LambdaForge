from lambda_terms import *

# Define the Church Numeral Addition function
ADD = Abstraction(
    Var("m"),
    Abstraction(
        Var("n"),
        Abstraction(
            Var("f"),
            Abstraction(
                Var("x"),
                FunctionApplication(
                    FunctionApplication(
                        Var("m"),
                        Var("f")
                    ),
                    FunctionApplication(
                        FunctionApplication(
                            Var("n"),
                            Var("f")
                        ),
                        Var("x")
                    )
                )
            )
        )
    )
)

# Define the Church Numeral Multiplication function
MULTIPLY = Abstraction(
    Var("m"),
    Abstraction(
        Var("n"),
        Abstraction(
            Var("f"),
            Abstraction(
                Var("x"),
                FunctionApplication(
                    FunctionApplication(
                        Var("m"),
                        FunctionApplication(Var("n"), Var("f"))
                    ),
                    Var("x")
                )
            )
        )
    )
)

# Define the Church Numeral Exponentiation function
EXPONENTIATE = Abstraction(
    Var("m"),
    Abstraction(
        Var("n"),
        FunctionApplication(
            FunctionApplication(
                Var("m"),
                FunctionApplication(
                    Var("n"),
                    Var("m")
                )
            ),
            Var("x")
        )
    )
)

TRUE = Abstraction(Var("x"), Abstraction(Var("y"), Var("x")))
FALSE = Abstraction(Var("x"), Abstraction(Var("y"), Var("y")))

OR = Abstraction(
    Var("p"),
    Abstraction(
        Var("q"),
        FunctionApplication(
            FunctionApplication(Var("p"), TRUE),
            Var("q")
        )
    )
)
AND = Abstraction(
    Var("p"),
    Abstraction(
        Var("q"),
        FunctionApplication(
            FunctionApplication(Var("p"), Var("q")),
            FALSE
        )
    )
)
NOT = Abstraction(
    Var("p"),
    FunctionApplication(
        FunctionApplication(Var("p"), FALSE),
        TRUE
    )
)