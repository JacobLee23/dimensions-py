"""
Unit tests for :py:mod:`dimensions.derived_units`.
"""

import typing

import pytest

from dimensions.base_units import (
    SECOND, METER, GRAM, AMPERE, KELVIN, MOLE, CANDELA
)
from dimensions import derived_units
from dimensions.derived_units import Unit
from dimensions.derived_units import UnitSequence


class TestUnitSequence:
    """
    Unit tests for :py:class:`UnitSequence`.
    """
    @pytest.mark.parametrize(
        "a, b, x", [
            (UnitSequence(), 1, True),
            (UnitSequence(), 1.0, True),
            (1, UnitSequence(), True),
            (1.0, UnitSequence(), True),

            (UnitSequence(SECOND), UnitSequence(SECOND), True),
            (UnitSequence(METER), UnitSequence(METER), True),
            (UnitSequence(GRAM), UnitSequence(GRAM), True),
            (UnitSequence(AMPERE), UnitSequence(AMPERE), True),
            (UnitSequence(KELVIN), UnitSequence(KELVIN), True),
            (UnitSequence(MOLE), UnitSequence(MOLE), True),
            (UnitSequence(CANDELA), UnitSequence(CANDELA), True),

            (UnitSequence(METER, METER), UnitSequence(METER, METER), True),
            (UnitSequence(METER, METER, METER), UnitSequence(METER, METER, METER), True),
            (UnitSequence(SECOND, AMPERE), UnitSequence(AMPERE, SECOND), True),

            (UnitSequence(METER, UnitSequence(METER, METER)),
             UnitSequence(UnitSequence(METER, METER), METER),
             True)
        ]
    )
    def test_eq(
            self,
            a: typing.Union[UnitSequence, int, float],
            b: typing.Union[UnitSequence, int, float],
            x: typing.Optional[bool]
    ):
        """

        :param a:
        :param b:
        :param x: The expected truth value of the expression ``a == b``
        """
        if x is None:
            with pytest.raises(ValueError):
                _ = a == b
                _ = a != b
        else:
            assert (a == b) is x, (a, b, x)
            assert (a != b) is not x, (a, b, x)

    @pytest.mark.parametrize(
        "a, x", [
            (UnitSequence(), False),
            (UnitSequence(SECOND), True),
            (UnitSequence(METER), True),
            (UnitSequence(GRAM), True),
            (UnitSequence(AMPERE), True),
            (UnitSequence(KELVIN), True),
            (UnitSequence(MOLE), True),
            (UnitSequence(CANDELA), True),
        ]
    )
    def test_bool(self, a: UnitSequence, x: bool):
        """

        :param a:
        :param x: The expected truth value of ``a``
        """
        assert bool(a) is x, a

    @pytest.mark.parametrize(
        "a, x", [
            (UnitSequence(), 0),
            (UnitSequence(SECOND), 1),
            (UnitSequence(AMPERE, SECOND), 2),
            (UnitSequence(METER, METER, METER), 3),
        ]
    )
    def test_len(self, a: UnitSequence, x: int):
        """

        :param a:
        :param x: The expected length of ``a``
        """
        assert len(a) == x, a

    @pytest.mark.parametrize(
        "a", [
            UnitSequence(),
            UnitSequence(SECOND),
            UnitSequence(AMPERE, SECOND),
            UnitSequence(METER, METER, METER),
        ]
    )
    def test_getitem(self, a: UnitSequence):
        """

        :param a:
        """
        for i, v in enumerate(a):
            assert a[i] == v, (a, i, v)

    @pytest.mark.parametrize(
        "a", [
            UnitSequence(),
            UnitSequence(SECOND),
            UnitSequence(AMPERE, SECOND),
            UnitSequence(METER, METER, METER),
        ]
    )
    def test_contains(self, a: UnitSequence):
        """

        :param a:
        """
        for v in a:
            assert v in a, (a, v)

    @pytest.mark.parametrize(
        "a, b, x", [
            (UnitSequence(), 0, 0),
            (UnitSequence(), 0.0, 0),
            (0, UnitSequence(), 0),
            (0.0, UnitSequence(), 0),

            (UnitSequence(), 1, UnitSequence()),
            (UnitSequence(), 1.0, UnitSequence()),
            (UnitSequence(SECOND), 1, UnitSequence(SECOND)),
            (UnitSequence(SECOND), 1.0, UnitSequence(SECOND)),
            (1, UnitSequence(), UnitSequence()),
            (1.0, UnitSequence(), UnitSequence()),
            (1, UnitSequence(SECOND), UnitSequence(SECOND)),
            (1.0, UnitSequence(SECOND), UnitSequence(SECOND)),
            (UnitSequence(), UnitSequence(), UnitSequence()),
            (UnitSequence(), UnitSequence(SECOND), UnitSequence(SECOND)),
            (UnitSequence(SECOND), UnitSequence(), UnitSequence(SECOND)),

            (UnitSequence(METER), UnitSequence(METER), UnitSequence(METER, METER)),
            (UnitSequence(AMPERE), UnitSequence(SECOND), UnitSequence(AMPERE, SECOND)),
            (UnitSequence(AMPERE), UnitSequence(SECOND), UnitSequence(SECOND, AMPERE)),
        ]
    )
    def test_mul(
            self,
            a: typing.Union[UnitSequence, int, float],
            b: typing.Union[UnitSequence, int, float],
            x: typing.Optional[UnitSequence]
    ):
        """

        :param a:
        :param b:
        :param x:
        """
        if x is None:
            with pytest.raises(TypeError):
                _ = a * b, (a, b, x)
        else:
            if isinstance(b, UnitSequence):
                assert a * b == b * a == x, (a, b, x)
            else:
                assert a * b == x, (a, b, x)

    @pytest.mark.parametrize(
        "a, b, x", [
            (UnitSequence(), UnitSequence(), UnitSequence()),
            (UnitSequence(), 1, UnitSequence()),
            (1, UnitSequence(), UnitSequence()),

            (UnitSequence(SECOND), UnitSequence(SECOND), UnitSequence()),
            (UnitSequence(SECOND), 1, UnitSequence(SECOND)),
            (1, UnitSequence(SECOND), UnitSequence(SECOND)),

            (0, UnitSequence(), 0),
            (0, UnitSequence(SECOND), 0),

            (UnitSequence(AMPERE, SECOND), UnitSequence(AMPERE), UnitSequence(SECOND)),
            (UnitSequence(AMPERE, SECOND), UnitSequence(SECOND), UnitSequence(AMPERE)),
            (UnitSequence(METER, METER), UnitSequence(METER), UnitSequence(METER)),
            (UnitSequence(METER, METER, METER), UnitSequence(METER), UnitSequence(METER, METER)),
            (UnitSequence(METER, METER, METER), UnitSequence(METER, METER), UnitSequence(METER)),

            (UnitSequence(GRAM, METER), UnitSequence(SECOND, SECOND), UnitSequence(GRAM, METER)),
            (UnitSequence(GRAM, METER),
             UnitSequence(METER, METER, SECOND, SECOND),
             UnitSequence(GRAM))
        ]
    )
    def test_truediv(
            self,
            a: typing.Union[UnitSequence, int, float],
            b: typing.Union[UnitSequence, int, float],
            x: typing.Optional[UnitSequence]
    ):
        """

        :param a:
        :param b:
        :param x:
        """
        if x is None:
            with pytest.raises(TypeError):
                _ = a / b, (a, b, x)
        else:
            assert a / b == x, (a, b, x)

    @pytest.mark.parametrize(
        "a, n, x", [
            (UnitSequence(), -1, None),
            (UnitSequence(), 0, UnitSequence()),
            (UnitSequence(), 1, UnitSequence()),
            (UnitSequence(), 2, UnitSequence()),

            (UnitSequence(METER), 0, UnitSequence()),
            (UnitSequence(METER), 1, UnitSequence(METER)),
            (UnitSequence(METER), 2, UnitSequence(METER, METER)),
            (UnitSequence(METER), 3, UnitSequence(METER, METER, METER)),
        ]
    )
    def test_pow(self, a: UnitSequence, n: int, x: typing.Optional[UnitSequence]):
        """

        :param a:
        :param n:
        :param x:
        """
        if x is None:
            if isinstance(n, int) and n < 0:
                with pytest.raises(ValueError):
                    _ = a ** n, (a, n, x)
            else:
                with pytest.raises(TypeError):
                    _ = a ** n, (a, n, x)
        else:
            assert a ** n == x, (a, n, x)


class TestUnit:
    """

    """

    @pytest.mark.parametrize(
        "a, b, x", [

        ]
    )
    def test_eq(self, a: Unit, b: Unit, x: typing.Optional[bool]):
        """

        :param a:
        :param b:
        :param x:
        :return:
        """
        if x is None:
            with pytest.raises(TypeError):
                _ = a == b, (a, b, x)
        assert a == b is x, (a, b, x)
