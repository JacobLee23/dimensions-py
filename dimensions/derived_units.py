"""

"""

import re
import typing

from .base_units import BaseUnit
from .base_units import (SECOND, METER, GRAM, AMPERE, KELVIN, MOLE, CANDELA)


class UnitSequence:
    """

    """
    def __init__(self, *args):
        """
        :param args:
        :type args: BaseUnit | UnitSequence
        :raise TypeError:
        """
        self._sequence = []
        for x in args:
            if isinstance(x, BaseUnit):
                self._sequence.append(x)
            elif isinstance(x, type(self)):
                self._sequence.extend(x.sequence)
            else:
                raise TypeError
        self._sequence = sorted(args, key=str)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.sequence})"

    def __eq__(self, other) -> bool:
        """
        :type other: UnitSequence
        :raise TypeError:
        """
        if isinstance(other, type(self)):
            return self.sequence == other.sequence
        elif isinstance(other, (int, float)):
            if other == 1:
                return self.sequence == []
            else:
                raise ValueError
        else:
            raise TypeError

    def __bool__(self) -> bool:
        return bool(self.sequence)

    def __len__(self) -> int:
        return len(self.sequence)

    def __getitem__(self, item: int) -> BaseUnit:
        return self.sequence[item]

    def __contains__(self, item) -> bool:
        return item in self.sequence

    def __mul__(self, other):
        """
        :type other: UnitSequence | int | float
        :rtype: UnitSequence
        :raise TypeError:
        """
        if isinstance(other, type(self)):
            return type(self)(*self.sequence, *other.sequence)
        elif isinstance(other, (int, float)):
            if other == 0:
                return 0
            elif other == 1:
                return type(self)(*self.sequence)
            else:
                raise ValueError
        else:
            raise TypeError

    def __rmul__(self, other):
        """
        :type other: UnitSequence | int | float
        :rtype: UnitSequence
        :raise TypeError:
        """
        return self * other

    def __truediv__(self, other):
        """
        :type other: UnitSequence
        :rtype: UnitSequence
        :raise TypeError:
        """
        if isinstance(other, type(self)):
            sequence = list(self.sequence)
            for unit in other.sequence:
                try:
                    sequence.remove(unit)
                except ValueError:
                    pass
            return type(self)(*sequence)
        elif isinstance(other, (int, float)):
            if other == 1:
                return type(self)(*self.sequence)
            else:
                raise ValueError
        else:
            raise TypeError

    def __rtruediv__(self, other):
        """
        :type other: UnitSequence
        :rtype: UnitSequence
        :raise TypeError:
        """
        if isinstance(other, type(self)):
            return other / self
        elif isinstance(other, (int, float)):
            if other == 0:
                return 0
            elif other == 1:
                return type(self)(*self.sequence)
            else:
                raise ValueError
        else:
            raise TypeError

    def __pow__(self, power: int, modulo: typing.Optional[int] = None):
        """
        :rtype: UnitSequence
        """
        if not isinstance(power, int):
            raise TypeError

        if power < 0:
            raise ValueError
        elif power == 0:
            return type(self)()
        else:
            return type(self)(*(self.sequence * power))

    @property
    def sequence(self) -> typing.List[BaseUnit]:
        """

        :return:
        """
        return self._sequence


class Unit:
    """

    """
    def __init__(self, numer, denom, name: str = "", abbr: str = ""):
        """

        :param numer:
        :type numer: list[BaseUnit] | UnitSequence | list[Unit]
        :param denom:
        :type denom: list[BaseUnit] | UnitSequence | list[Unit]
        :param name:
        :param abbr:
        """
        unitsn, unitsd = [], []
        for unit in numer:
            if isinstance(unit, BaseUnit):
                unitsn.append(unit)
            elif isinstance(unit, Unit):
                unitsn.extend(unit.numerator)
                unitsd.extend(unit.denominator)
            else:
                raise TypeError
        for unit in denom:
            if isinstance(unit, BaseUnit):
                unitsd.append(unit)
            elif isinstance(unit, Unit):
                unitsd.extend(unit.numerator)
                unitsn.extend(unit.denominator)
            else:
                raise TypeError
        numerator, denominator = UnitSequence(*unitsn), UnitSequence(*unitsd)

        self._numer = numerator / denominator
        self._denom = denominator / numerator

        self._name = name
        self._abbr = abbr

    def __repr__(self) -> str:
        args = (
            f"numerator={self.numerator}",
            f"denominator={self.denominator}",
            f"name={self.name}",
            f"abbr={self.abbr}"
        )
        return f"{type(self).__name__}({', '.join(args)})"

    def __str__(self) -> str:
        return self.abbr

    def __eq__(self, other) -> bool:
        """

        :param other:
        :return:
        """
        if not isinstance(other, Unit):
            raise TypeError

        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __bool__(self) -> bool:
        return bool(self.numerator) and bool(self.denominator)

    def __len__(self) -> typing.Tuple[int, int]:
        return len(self.numerator), len(self.denominator)

    def __getitem__(self, item) -> UnitSequence:
        """
        :type item:
        :raise TypeError:
        :raise ValueError:
        """
        if not isinstance(item, (int, str)):
            raise TypeError

        if item == 0 or re.search(r"n(umer(ator)?)?", item, re.IGNORECASE):
            return self.numerator
        elif item == 1 or re.search(r"d(enom(inator)?)?", item, re.IGNORECASE):
            return self.denominator
        else:
            raise ValueError

    def __contains__(self, item: typing.Any) -> bool:
        return item in self.numerator or item in self.denominator

    def __mul__(self, other):
        """
        :param other:
        :rtype: Unit
        :raise TypeError:
        """
        if not isinstance(other, Unit):
            raise TypeError

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return type(self)(
            numerator / denominator, denominator / numerator
        )

    def __truediv__(self, other):
        """
        :param other:
        :rtype: Unit
        :raise TypeError:
        """
        if not isinstance(other, Unit):
            raise TypeError

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return type(self)(
            numerator / denominator, denominator / numerator
        )

    def __pow__(self, power: int, modulo: typing.Optional[int] = None):
        """
        :rtype: Unit
        """
        if not isinstance(power, int):
            raise ValueError

        if power < 0:
            return type(self)(self.denominator ** abs(power), self.numerator ** abs(power))
        elif power == 0:
            return type(self)([], [])
        else:
            return type(self)(self.numerator ** power, self.denominator ** power)

    @property
    def numerator(self) -> UnitSequence:
        """

        :return:
        """
        return self._numer

    @property
    def denominator(self) -> UnitSequence:
        """

        :return:
        """
        return self._denom

    @property
    def name(self) -> str:
        """

        :return:
        """
        return self._name

    @property
    def abbr(self) -> str:
        """

        :return:
        """
        return self._abbr

    @property
    def si_bu_equivalent(self) -> str:
        """

        :return:
        """
        return f"{' * '.join(self.numerator)} / {' * '.join(self.denominator)}"

    def si_bu_latex(self, *, fraction=False) -> str:
        """

        :return:
        """
        countn = {x: list(self.numerator).count(x) for x in set(self.numerator)}
        countd = {x: list(self.denominator).count(x) for x in set(self.denominator)}
        if fraction:
            numerator = " * ".join(f"{k}^{{{v}}}" for k, v in countn.values())
            denominator = " * ".join(f"{k}^{{{v}}}" for k, v in countd.values())
            return fr"$\frac{{{numerator}}}{{{denominator}}}$"
        else:
            numerator = " * ".join(f"{k}^{{{v}}}" for k, v in countn.values())
            denominator = " * ".join(f"{k}^{{{-v}}}" for k, v in countd.values())
            return fr"${numerator} * {denominator}$"

    @classmethod
    def factory(cls, name: str, *args, **kwargs):
        """

        :param name:
        :param args:
        :param kwargs:
        :return:
        """
        def __init__(self):
            cls.__init__(self, *args, **kwargs)

        return type(name, (cls,), {"__init__": __init__})()


# SI Base Units
Second = Unit.factory("Second", [SECOND], [], "second", "s")
Meter = Unit.factory("Meter", [METER], [], "meter", "m")
Gram = Unit.factory("Gram", [GRAM], [], "gram", "g")
Ampere = Unit.factory("Ampere", [AMPERE], [], "ampere", "A")
Kelvin = Unit.factory("Kelvin", [KELVIN], [], "kelvin", "K")
Mole = Unit.factory("Mole", [MOLE], [], "mole", "mol")
Candela = Unit.factory("Candela", [CANDELA], [], "candela", "cd")


# Named SI Derived Units
# TODO: Newton, Gray, Sievert: g -> kg
Hertz = Unit.factory("Hertz", [], [Second], "Hertz", "Hz")
Radian = Unit.factory("Radian", [Meter], [Meter], "radian", "rad")
Steradian = Unit.factory("Steradian", [Meter, Meter], [Meter, Meter], "steradian", "sr")
Newton = Unit.factory("Newton", [Gram, Meter], [Second, Second], "newton", "N")
Pascal = Unit.factory("Newton", [Newton], [Meter, Meter], "pascal", "Pa")
Joule = Unit.factory("Joule", [Meter, Newton], [], "joule", "J")
Watt = Unit.factory("Watt", [Joule], [Second], "watt", "W")
Coulomb = Unit.factory("Coulomb", [Second, Ampere], [], "coulomb", "C")
Volt = Unit.factory("Volt", [Watt], [Ampere], "volt", "V")
Farad = Unit.factory("Farad", [Coulomb], [Volt], "farad", "F")
Ohm = Unit.factory("Ohm", [Volt], [Ampere], "ohm", "Ω")
Siemens = Unit.factory("Siemens", [], [Ohm], "siemens", "S")
Weber = Unit.factory("Weber", [Joule], [Ampere], "weber", "Wb")
Tesla = Unit.factory("Tesla", [Volt, Second], [Meter, Meter], "tesla", "T")
Henry = Unit.factory("Henry", [Volt, Second], [Ampere], "henry", "H")
Celsius = Unit.factory("Celsius", [Kelvin], [], "celsius", "°C")
Lumen = Unit.factory("Lumen", [Candela, Steradian], [], "lumen", "lm")
Lux = Unit.factory("Lux", [Lumen], [Meter, Meter], "lux", "lx")
Becquerel = Unit.factory("Becquerel", [], [Second], "becquerel", "Bq")
Gray = Unit.factory("Gray", [Joule], [Gram], "gray", "Gy")
Sievert = Unit.factory("Sievert", [Joule], [Gram], "sievert", "Sv")
Katal = Unit.factory("Katal", [Mole], [Second], "katal", "kat")
