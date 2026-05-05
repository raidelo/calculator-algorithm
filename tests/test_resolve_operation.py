from calculator_algorithm.utils.recursive import (
    resolve_operation as resolve_operation_recursive,
)
from tests.conftest import TestDataType


def test_resolve_operation_recursive(test_data: TestDataType) -> None:
    for _, _, operation, desired_result in test_data:
        result = resolve_operation_recursive(operation)
        assert result == desired_result
