from abc import abstractmethod
from typing import Protocol, TypeVar, Iterable


def proper_values(values: Iterable) -> list:
    proper_values = []
    for v in values:
        if isinstance(v, str):
            proper_values.append(f'"{v}"')
        elif v is None:
            proper_values.append('NULL')
        else:
            proper_values.append(f'{v}')
    return proper_values
