from calculator_algorithm.types_ import Atom, Operation, Operator


def test_operation_to_str() -> None:
    data = [
        (Operation(Operator.ADD, Atom(12), Atom(25)), "( 12 + 25 )"),
        (
            Operation(
                Operator.ADD,
                Atom(12),
                Operation(Operator.MULTIPLY, Atom(47), Atom(9)),
            ),
            "( 12 + ( 47 * 9 ) )",
        ),
        (
            Operation(
                Operator.ADD,
                Operation(Operator.MULTIPLY, Atom(47), Atom(9)),
                Atom(12),
            ),
            "( ( 47 * 9 ) + 12 )",
        ),
        (
            Operation(
                Operator.DIVIDE,
                Operation(Operator.MULTIPLY, Atom(67), Atom(3)),
                Operation(Operator.SUBTRACT, Atom(332), Atom(7)),
            ),
            "( ( 67 * 3 ) / ( 332 - 7 ) )",
        ),
    ]

    for operation, desired_str in data:
        assert str(operation) == desired_str
