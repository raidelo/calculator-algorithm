from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto

from calculator_algorithm.errors import InvalidOperator

type Token = Atom | Operator


class Atom(Decimal):
    pass


class Operator(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    @classmethod
    def from_symbol(cls, symbol: str) -> Operator:
        match symbol:
            case "+":
                return cls.ADD
            case "-":
                return cls.SUBTRACT
            case "*":
                return cls.MULTIPLY
            case "/":
                return cls.DIVIDE
            case _:
                raise InvalidOperator(symbol)

    def __str__(self) -> str:
        match self:
            case self.ADD:
                return "+"
            case self.SUBTRACT:
                return "-"
            case self.MULTIPLY:
                return "*"
            case self.DIVIDE:
                return "/"

    def __repr__(self) -> str:
        return str(self)


@dataclass
class Operation:
    operator: Operator
    left: Atom | Operation
    right: Atom | Operation

    def __str__(self) -> str:
        return f"( {self.left} {self.operator} {self.right} )"
