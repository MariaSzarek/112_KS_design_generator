import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from points import Point

@pytest.fixture
def point1():
    return Point(1, 2)


@pytest.fixture
def point2():
    return Point(1, 2)


@pytest.fixture
def point3():
    return Point(2, 2)


@pytest.fixture
def point4():
    return Point(3, 4)


def test_init(point1):
    assert point1.x == 1
    assert point1.y == 2


def test_eq(point1, point2, point3):
    assert point1 == point2
    assert point1 != point3


def test_lt(point1, point3, point4):
    assert point1 < point3
    assert point3 < point4
    assert not (point3 < point1)


def test_hash(point1, point2, point3):
    assert hash(point1) == hash(point2)
    assert hash(point1) != hash(point3)


def test_distance(point1, point4):
    assert point1.distance(point4) == 2.8284271247461903
    assert point1.distance(point1) == 0