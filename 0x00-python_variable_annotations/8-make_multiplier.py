#!/usr/bin/env python3
""" Module documentation """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Func documents"""

    def mult(m: float) -> float:
        """Func doc"""
        return m * multiplier

    return mult
