"""
Unit tests for :py:mod:`dimensions.derived_units`.
"""

import typing

import pytest

from dimensions.base_units import (
    SECOND, METER, GRAM, AMPERE, KELVIN, MOLE, CANDELA
)
from dimensions import derived_units


class TestUnitSequence:
    """
    Unit tests for :py:class:`derived_units.UnitSequence`.
    """
    @pytest.mark.parametrize(
        "a, b, eq", [
            (derived_units.UnitSequence(), 1, True),
            (derived_units.UnitSequence(), 1.0, True),
            (1, derived_units.UnitSequence(), True),
            (1.0, derived_units.UnitSequence(), True),

            (derived_units.UnitSequence(SECOND),
             derived_units.UnitSequence(SECOND),
             True),
            (derived_units.UnitSequence(METER),
             derived_units.UnitSequence(METER),
             True),
            (derived_units.UnitSequence(GRAM),
             derived_units.UnitSequence(GRAM),
             True),
            (derived_units.UnitSequence(AMPERE),
             derived_units.UnitSequence(AMPERE),
             True),
            (derived_units.UnitSequence(KELVIN),
             derived_units.UnitSequence(KELVIN),
             True),
            (derived_units.UnitSequence(MOLE),
             derived_units.UnitSequence(MOLE),
             True),
            (derived_units.UnitSequence(CANDELA),
             derived_units.UnitSequence(CANDELA),
             True),

            (derived_units.UnitSequence(METER, METER),
             derived_units.UnitSequence(METER, METER),
             True),
            (derived_units.UnitSequence(METER, METER, METER),
             derived_units.UnitSequence(METER, METER, METER),
             True),
            (derived_units.UnitSequence(SECOND, AMPERE),
             (derived_units.UnitSequence(AMPERE, SECOND)),
             True),

            (derived_units.UnitSequence(METER, derived_units.UnitSequence(METER, METER)),
             derived_units.UnitSequence(derived_units.UnitSequence(METER, METER), METER),
             True)
        ]
    )
    def test_eq(
            self,
            a: derived_units.UnitSequence,
            b: derived_units.UnitSequence,
            eq: typing.Optional[bool]
    ):
        """

        :param a:
        :param b:
        :param eq: The expected truth value of the expression ``a == b``
        """
        if eq is None:
            with pytest.raises(ValueError):
                _ = a == b
                _ = a != b
        else:
            assert (a == b) is eq, (a, b, eq)
            assert (a != b) is not eq, (a, b, eq)

    @pytest.mark.parametrize(
        "a, x", [
            (derived_units.UnitSequence(), False),
            (derived_units.UnitSequence(SECOND), True),
            (derived_units.UnitSequence(METER), True),
            (derived_units.UnitSequence(GRAM), True),
            (derived_units.UnitSequence(AMPERE), True),
            (derived_units.UnitSequence(KELVIN), True),
            (derived_units.UnitSequence(MOLE), True),
            (derived_units.UnitSequence(CANDELA), True),
        ]
    )
    def test_bool(self, a: derived_units.UnitSequence, x: bool):
        """

        :param a:
        :param x: The expected truth value of ``a``
        """
        assert bool(a) is x, a

    @pytest.mark.parametrize(
        "a, x", [
            (derived_units.UnitSequence(), 0),
            (derived_units.UnitSequence(SECOND), 1),
            (derived_units.UnitSequence(AMPERE, SECOND), 2),
            (derived_units.UnitSequence(METER, METER, METER), 3),
        ]
    )
    def test_len(self, a: derived_units.UnitSequence, x: int):
        """

        :param a:
        :param x: The expected length of ``a``
        """
        assert len(a) == x, a

    @pytest.mark.parametrize(
        "a", [
            derived_units.UnitSequence(),
            derived_units.UnitSequence(SECOND),
            derived_units.UnitSequence(AMPERE, SECOND),
            derived_units.UnitSequence(METER, METER, METER),
        ]
    )
    def test_getitem(self, a: derived_units.UnitSequence):
        """

        :param a:
        """
        for i, v in enumerate(a):
            assert a[i] == v, (a, i, v)

    @pytest.mark.parametrize(
        "a", [
            derived_units.UnitSequence(),
            derived_units.UnitSequence(SECOND),
            derived_units.UnitSequence(AMPERE, SECOND),
            derived_units.UnitSequence(METER, METER, METER),
        ]
    )
    def test_contains(self, a: derived_units.UnitSequence):
        """

        :param a:
        """
        for v in a:
            assert v in a, (a, v)

    @pytest.mark.parametrize(
        "a, b, x", [
            (derived_units.UnitSequence(), 0, 0),
            (derived_units.UnitSequence(), 0.0, 0),
            (0, derived_units.UnitSequence(), 0),
            (0.0, derived_units.UnitSequence(), 0),

            (derived_units.UnitSequence(), 1, derived_units.UnitSequence()),
            (derived_units.UnitSequence(), 1.0, derived_units.UnitSequence()),
            (derived_units.UnitSequence(SECOND), 1, derived_units.UnitSequence(SECOND)),
            (derived_units.UnitSequence(SECOND), 1.0, derived_units.UnitSequence(SECOND)),
            (1, derived_units.UnitSequence(), derived_units.UnitSequence()),
            (1.0, derived_units.UnitSequence(), derived_units.UnitSequence()),
            (1, derived_units.UnitSequence(SECOND), derived_units.UnitSequence(SECOND)),
            (1.0, derived_units.UnitSequence(SECOND), derived_units.UnitSequence(SECOND)),
            (derived_units.UnitSequence(), derived_units.UnitSequence(), derived_units.UnitSequence()),
            (derived_units.UnitSequence(),
             derived_units.UnitSequence(SECOND),
             derived_units.UnitSequence(SECOND)),
            (derived_units.UnitSequence(SECOND),
             derived_units.UnitSequence(),
             derived_units.UnitSequence(SECOND)),

            (derived_units.UnitSequence(METER),
             derived_units.UnitSequence(METER),
             derived_units.UnitSequence(METER, METER)),
            (derived_units.UnitSequence(AMPERE),
             derived_units.UnitSequence(SECOND),
             derived_units.UnitSequence(AMPERE, SECOND)),
            (derived_units.UnitSequence(AMPERE),
             derived_units.UnitSequence(SECOND),
             derived_units.UnitSequence(SECOND, AMPERE)),
        ]
    )
    def test_mul(
            self,
            a: typing.Union[derived_units.UnitSequence, int, float],
            b: typing.Union[derived_units.UnitSequence, int, float],
            x: typing.Optional[derived_units.UnitSequence]
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
            if isinstance(b, derived_units.UnitSequence):
                assert a * b == b * a == x, (a, b, x)
            else:
                assert a * b == x, (a, b, x)

    @pytest.mark.parametrize(
        "a, b, x", [

        ]
    )
    def test_floordiv(
            self,
            a: typing.Union[derived_units.UnitSequence, int, float],
            b: typing.Union[derived_units.UnitSequence, int, float],
            x: typing.Optional[derived_units.UnitSequence]
    ):
        """

        :param a:
        :param b:
        :param x:
        """
        if x is None:
            with pytest.raises(TypeError):
                _ = a // b, (a, b, x)
        else:
            assert a // b == x, (a, b, x)

    @pytest.mark.parametrize(
        "a, b, x", [

        ]
    )
    def test_mod(
            self,
            a: typing.Union[derived_units.UnitSequence, int, float],
            b: typing.Union[derived_units.UnitSequence, int, float],
            x: typing.Optional[derived_units.UnitSequence]
    ):
        """

        :param a:
        :param b:
        :param x:
        """
        if x is None:
            with pytest.raises(TypeError):
                _ = a % b, (a, b, x)
        else:
            assert a % b == x, (a, b, x)
