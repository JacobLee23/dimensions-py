"""
Unit tests for :py:mod:`dimensions.base_units`.
"""

import typing

import pytest

from dimensions import base_units as bu
from dimensions.base_units import (
    SECOND, METER, GRAM, AMPERE, KELVIN, MOLE, CANDELA
)


class TestBaseUnit:
    """
    Unit tests for :py:class:`base_units.BaseUnit`.
    """

    @pytest.mark.parametrize(
        "a, b, eq", [
            # Equality between identical instances
            (SECOND, SECOND, True),
            (METER, METER, True),
            (GRAM, GRAM, True),
            (AMPERE, AMPERE, True),
            (KELVIN, KELVIN, True),
            (MOLE, MOLE, True),
            (CANDELA, CANDELA, True),

            # Equality between non-identical instances
            (bu.Second(), bu.Second(), True),
            (bu.Meter(), bu.Meter(), True),
            (bu.Gram(), bu.Gram(), True),
            (bu.Ampere(), bu.Ampere(), True),
            (bu.Kelvin(), bu.Kelvin(), True),
            (bu.Mole(), bu.Mole(), True),
            (bu.Candela(), bu.Candela(), True),

            # Inequality between identical (inherited) types
            (SECOND, METER, False),
            (METER, GRAM, False),
            (GRAM, AMPERE, False),
            (AMPERE, KELVIN, False),
            (KELVIN, MOLE, False),
            (MOLE, CANDELA, False),
            (CANDELA, SECOND, False),

            # Invalid comparison between differing types
            (SECOND, True, None),
            (METER, 0, None),
            (GRAM, 0.0, None),
            (AMPERE, "", None),
            (KELVIN, [], None),
            (MOLE, (), None),
            (CANDELA, {}, None),
        ]
    )
    def test_eq(self, a: bu.BaseUnit, b: bu.BaseUnit, eq: typing.Optional[bool]):
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
