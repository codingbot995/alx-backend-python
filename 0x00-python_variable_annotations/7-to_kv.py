#!/usr/bin/env python3
'''fun'''
from typing import Tuple, Union

def to_kv(k: str, v:Union[ int, float)] -> Tuple[str, float]:
    return (k, v **2)
