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
            # Multiplicative identity
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

            # Multiplicative commutativity
            (derived_units.UnitSequence(METER, METER),
             derived_units.UnitSequence(METER, METER),
             True),
            (derived_units.UnitSequence(METER, METER, METER),
             derived_units.UnitSequence(METER, METER, METER),
             True),
            (derived_units.UnitSequence(SECOND, AMPERE),
             (derived_units.UnitSequence(AMPERE, SECOND)),
             True),

            # Multiplicative associativity
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
        :param eq:
        """
        if eq is None:
            with pytest.raises(TypeError):
                assert a == b
                assert a != b
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
        :param x:
        """
        assert bool(a) is x, a
