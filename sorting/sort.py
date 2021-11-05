from __future__ import annotations
from collections import Counter
from itertools import chain
from typing import Iterable, List, TypeVar


T = TypeVar('T')


def pseudo_index(value, min_, max_, n) -> int:
    """Return an approximate index where to put a value in a sorted list"""
    return int((n - 1) * (value - min_) / (max_ - min_))


def sort_unique(values: List[T]) -> Iterable[T]:
    """Sort list of values, where every value occurs exactly once"""
    if len(values) == 1:
        return values
    value_iterator = iter(values)
    min_ = max_ = next(value_iterator)
    for val in value_iterator:
        if val > max_: max_ = val
        elif val < min_: min_ = val
    result = [[] for _ in range(len(values))]
    for val in values:
        result[pseudo_index(val, min_, max_, len(values))].append(val)
    return chain.from_iterable(sort_unique(val) for val in result if val)


def sort_list(values: Iterable[T]) -> Iterable[T]:
    """Sort iterable of values"""
    cnt = Counter()
    for val in values:
        cnt[val] += 1
    return list(chain.from_iterable((val for _ in range(cnt[val])) for val in sort_unique(cnt.keys())))
