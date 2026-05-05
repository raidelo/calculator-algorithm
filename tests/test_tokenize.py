from calculator_algorithm.utils import tokenize
from tests.conftest import TestDataType


def test_tokenize(test_data: TestDataType) -> None:
    for text, desired_tokens, _, _ in test_data:
        tokens = tokenize(text)
        assert tokens == desired_tokens
