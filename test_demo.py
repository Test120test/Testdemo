from demo import *
import pytest


def test_add():
    assert add_func(1,2) == 3

def test_sub():
    assert sub_func(1,2) == -1

def test_mul():
    assert mul_func(1,2) == 2
