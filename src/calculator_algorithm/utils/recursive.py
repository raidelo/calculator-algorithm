from calculator_algorithm.types_ import Atom, Operation
from calculator_algorithm.utils import operate
from calculator_algorithm.utils.helpers import isatom


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
