from decimal import DivisionByZero, InvalidOperation

from calculator_algorithm.errors import InvalidOperator, InvalidTokenSequence
from calculator_algorithm.utils import tokenize
from calculator_algorithm.utils.recursive import resolve_operation, tokens_to_operation

PROMPT = ">> "


def main() -> None:
    while True:
        inp = input(PROMPT)

        if inp.lower() in ["q", "quit", "exit"]:
            break

        try:
            tokens = tokenize(inp)
        except InvalidOperation:
            print(f"error: Invalid operation: {inp!r}")
            return
        except InvalidOperator as e:
            print(f"error: Invalid operator: {e.args[0]!r}")
            return

        try:
            operation = tokens_to_operation(tokens)
        except InvalidTokenSequence:
            print(f"error: Invalid expression: {inp!r}")
            return

        try:
            solution = resolve_operation(operation)
        except DivisionByZero:
            print(f"error: Can't divide by zero: {inp!r}")
            return

        print(solution)

    print("\nExitting ...")
