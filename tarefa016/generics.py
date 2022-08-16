from typing import TypeVar, List

T = TypeVar("T")


def first(container: List[T]) -> T:
    return container[0]
