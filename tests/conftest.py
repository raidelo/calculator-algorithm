from pytest import fixture

from calculator_algorithm.types_ import Atom, Operation, Operator, Token

type TestDataType = list[tuple[str, list[Token], Operation, Atom]]


@fixture
def test_data() -> TestDataType:
    return [
        (
            "3 + 9",
            [Atom(3), Operator.ADD, Atom(9)],
            Operation(Operator.ADD, Atom(3), Atom(9)),
            Atom(12),
        ),
        (
            "5 - 3",
            [Atom(5), Operator.SUBTRACT, Atom(3)],
            Operation(Operator.SUBTRACT, Atom(5), Atom(3)),
            Atom(2),
        ),
        (
            "9 * 5",
            [Atom(9), Operator.MULTIPLY, Atom(5)],
            Operation(Operator.MULTIPLY, Atom(9), Atom(5)),
            Atom(45),
        ),
        (
            "60 / 2",
            [Atom(60), Operator.DIVIDE, Atom(2)],
            Operation(Operator.DIVIDE, Atom(60), Atom(2)),
            Atom(30),
        ),
        (
            "60 + 9 * 5",
            [Atom(60), Operator.ADD, Atom(9), Operator.MULTIPLY, Atom(5)],
            Operation(
                Operator.ADD,
                Atom(60),
                Operation(Operator.MULTIPLY, Atom(9), Atom(5)),
            ),
            Atom(105),
        ),
        (
            "55 / 5 - 60",
            [Atom(55), Operator.DIVIDE, Atom(5), Operator.SUBTRACT, Atom(60)],
            Operation(
                Operator.SUBTRACT,
                Operation(Operator.DIVIDE, Atom(55), Atom(5)),
                Atom(60),
            ),
            Atom(-49),
        ),
        (
            "60 / 12 - 25 * 2",
            [
                Atom(60),
                Operator.DIVIDE,
                Atom(12),
                Operator.SUBTRACT,
                Atom(25),
                Operator.MULTIPLY,
                Atom(2),
            ],
            Operation(
                Operator.SUBTRACT,
                Operation(Operator.DIVIDE, Atom(60), Atom(12)),
                Operation(Operator.MULTIPLY, Atom(25), Atom(2)),
            ),
            Atom(-45),
        ),
        (
            "3 * 4 * 5 + 6",
            [
                Atom(3),
                Operator.MULTIPLY,
                Atom(4),
                Operator.MULTIPLY,
                Atom(5),
                Operator.ADD,
                Atom(6),
            ],
            Operation(
                Operator.ADD,
                Operation(
                    Operator.MULTIPLY,
                    Atom(3),
                    Operation(Operator.MULTIPLY, Atom(4), Atom(5)),
                ),
                Atom(6),
            ),
            Atom(66),
        ),
    ]
