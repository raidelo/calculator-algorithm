from enum import Enum, auto
from typing import Literal

from calculator_algorithm.constants import ADD_SUBTRACT_GLUES, MULTIPLY_DIVIDE_GLUES
from calculator_algorithm.errors import InvalidExpression
from calculator_algorithm.types_ import Atom, Operator, Token


def tokenize(text: str) -> list[Token]:
    parts = text.strip().split()

    tokens: list[Token] = []

    class Turn(Enum):
        ATOM = auto()
        OPERATOR = auto()

    turn = Turn.ATOM
    for part in parts:
        error = False

        match turn:
            case Turn.ATOM:
                try:
                    tokens.append(Atom(part))
                    turn = Turn.OPERATOR
                except ValueError:
                    error = True

            case Turn.OPERATOR:
                try:
                    op = Operator.from_symbol(part)
                    tokens.append(op)
                    turn = Turn.ATOM
                except TypeError:
                    error = True

        if error:
            raise InvalidExpression(text)

    return tokens


def operate(operator: Operator, left: Atom, right: Atom) -> Atom:
    match operator:
        case Operator.ADD:
            return left + right
        case Operator.SUBTRACT:
            return left - right
        case Operator.MULTIPLY:
            return left * right
        case Operator.DIVIDE:
            return left / right


def get_glue_for(
    operator: Operator,
) -> tuple[Literal[0], Literal[1]] | tuple[Literal[2], Literal[3]]:
    glue = 0
    match operator:
        case Operator.ADD | Operator.SUBTRACT:
            glue = ADD_SUBTRACT_GLUES
        case Operator.MULTIPLY | Operator.DIVIDE:
            glue = MULTIPLY_DIVIDE_GLUES

    return glue
