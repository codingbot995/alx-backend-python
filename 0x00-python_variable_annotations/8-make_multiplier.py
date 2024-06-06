#!/usr/bin/env python3

from typing import Callable

def make_multiplie(multiplier: float) -> Callable[[float], float]:
    def mult(m: float) -> float:
        return m * multiplier
    return mult
