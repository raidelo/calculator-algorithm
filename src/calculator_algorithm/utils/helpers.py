from decimal import Decimal
from typing import Any, TypeIs

from calculator_algorithm.types_ import Atom, Operation, Operator


def isatom(item: Any) -> TypeIs[Atom]:
    return isinstance(item, Decimal)


def isoperation(item: Any) -> TypeIs[Operation]:
    return isinstance(item, Operation)


def isoperator(item: Any) -> TypeIs[Operator]:
    return isinstance(item, Operator)
