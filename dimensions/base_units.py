"""
Definitions for representations of the 7 SI base units (`Wikipedia`_).

.. _Wikipedia: https://en.wikipedia.org/wiki/SI_base_unit

.. py:data:: SECOND

.. py:data:: METER

.. py:data:: GRAM

.. py:data:: AMPERE

.. py:data:: KELVIN

.. py:data:: MOLE

.. py:data:: CANDELA
"""


class BaseUnit:
    """

    """
    def __init__(self, name: str, abbr: str):
        """
        :param name: The SI name of the unit
        :param abbr: The SI abbreviation for the unit
        """
        self._name = name
        self._abbr = abbr

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, abbr={self.abbr})"

    def __str__(self) -> str:
        return self.abbr

    def __eq__(self, other) -> bool:
        """
        :type other: BaseUnit
        :raise TypeError:
        """
        if not issubclass(type(other), BaseUnit):
            raise TypeError

        return type(self) == type(other)

    @property
    def abbr(self) -> str:
        """
        :return: The SI abbreviation for the unit
        """
        return self._abbr

    @property
    def name(self) -> str:
        """
        :return: The SI name of the unit
        """
        return self._name


SECOND = BaseUnit("second", "s")
METER = BaseUnit("meter", "m")
GRAM = BaseUnit("gram", "g")
AMPERE = BaseUnit("ampere", "A")
KELVIN = BaseUnit("kelvin", "K")
MOLE = BaseUnit("mole", "mol")
CANDELA = BaseUnit("candela", "cd")
