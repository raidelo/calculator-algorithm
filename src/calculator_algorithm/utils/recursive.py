from calculator_algorithm.errors import InvalidTokenSequence
from calculator_algorithm.types_ import Atom, Operation, Token
from calculator_algorithm.utils import get_glue_for, operate
from calculator_algorithm.utils.helpers import isatom, isoperator


def resolve_operation(operation: Operation | Atom) -> Atom:
    if isatom(operation):
        return operation

    if isatom(operation.left) and isatom(operation.right):
        return operate(operation.operator, operation.left, operation.right)

    return resolve_operation(
        Operation(
            operation.operator,
            resolve_operation(operation.left),
            resolve_operation(operation.right),
        )
    )


def tokens_to_operation(tokens: list[Token]) -> Operation | Atom:
    result, _ = _tokens_to_operation(tokens)
    return result


def _tokens_to_operation(
    tokens: list[Token],
    index: int = 0,
    last_op_right_glue: int = 0,
) -> tuple[Operation | Atom, int]:
    try:
        left: Operation | Token = tokens[index]
        if not isatom(left):
            raise TypeError(left, Atom)
    except IndexError as e:
        raise InvalidTokenSequence(tokens) from e

    index += 1

    while index < len(tokens):
        op = tokens[index]
        if not isoperator(op):
            break

        op_left_glue, op_right_glue = get_glue_for(op)

        if last_op_right_glue > op_left_glue:
            break

        right, index = _tokens_to_operation(
            tokens, index + 1, last_op_right_glue=op_right_glue
        )

        left = Operation(operator=op, left=left, right=right)

    return left, index
