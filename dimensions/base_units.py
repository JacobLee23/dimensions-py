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
        if not isinstance(other, BaseUnit):
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

    @classmethod
    def factory(cls, name: str, *args, **kwargs):
        """

        :return:
        """
        def __init__(self):
            cls.__init__(self, *args, **kwargs)

        return type(name, (cls,), {"__init__": __init__})()


SECOND = BaseUnit.factory("Second", "second", "s")
METER = BaseUnit.factory("Meter", "meter", "m")
GRAM = BaseUnit.factory("Gram", "gram", "g")
AMPERE = BaseUnit.factory("Ampere", "ampere", "A")
KELVIN = BaseUnit.factory("Kelvin", "kelvin", "K")
MOLE = BaseUnit.factory("Mole", "mole", "mol")
CANDELA = BaseUnit.factory("Candela", "candela", "cd")
