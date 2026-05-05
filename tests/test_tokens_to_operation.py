from calculator_algorithm.utils.recursive import tokens_to_operation
from tests.conftest import TestDataType


def test_tokens_to_operation(test_data: TestDataType) -> None:
    for _, tokens, desired_operation, _ in test_data:
        operation = tokens_to_operation(tokens)
        assert operation == desired_operation
