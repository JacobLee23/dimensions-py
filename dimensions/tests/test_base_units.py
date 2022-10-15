"""
Unit tests for :py:mod:`dimensions.base_units`.
"""

import typing

import pytest

from dimensions import base_units


class TestBaseUnit:
    """
    Unit tests for :py:class:`base_units.BaseUnit`.
    """

    @pytest.mark.parametrize(
        "a, b, eq", [
            # Equality between identical instances
            (base_units.SECOND, base_units.SECOND, True),
            (base_units.METER, base_units.METER, True),
            (base_units.AMPERE, base_units.AMPERE, True),
            (base_units.GRAM, base_units.GRAM, True),
            (base_units.KELVIN, base_units.KELVIN, True),
            (base_units.MOLE, base_units.MOLE, True),
            (base_units.CANDELA, base_units.CANDELA, True),

            # Equality between non-identical instances
            (base_units.Second(), base_units.Second(), True),
            (base_units.Meter(), base_units.Meter(), True),
            (base_units.Ampere(), base_units.Ampere(), True),
            (base_units.Gram(), base_units.Gram(), True),
            (base_units.Kelvin(), base_units.Kelvin(), True),
            (base_units.Mole(), base_units.Mole(), True),
            (base_units.Candela(), base_units.Candela(), True),

            # Inequality between identical (inherited) types
            (base_units.SECOND, base_units.METER, False),
            (base_units.METER, base_units.GRAM, False),
            (base_units.GRAM, base_units.AMPERE, False),
            (base_units.AMPERE, base_units.KELVIN, False),
            (base_units.KELVIN, base_units.MOLE, False),
            (base_units.MOLE, base_units.CANDELA, False),
            (base_units.CANDELA, base_units.SECOND, False),

            # Invalid comparison between differing types
            (base_units.SECOND, True, None),
            (base_units.METER, 0, None),
            (base_units.AMPERE, 0.0, None),
            (base_units.GRAM, "", None),
            (base_units.KELVIN, [], None),
            (base_units.MOLE, (), None),
            (base_units.CANDELA, {}, None),
        ]
    )
    def test_eq(
            self,
            a: base_units.BaseUnit,
            b: base_units.BaseUnit,
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
