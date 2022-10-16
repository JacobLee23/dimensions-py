"""

"""

from decimal import Decimal
import typing


class SIPrefix:
    """

    """
    def __init__(self, scale: Decimal, name: str = "", abbr: str = ""):
        """
        :param scale:
        :param name:
        :param abbr:
        """
        if scale % Decimal(10) != 0:
            raise ValueError

        self._scale = scale
        self._name = name
        self._abbr = abbr

    def __repr__(self) -> str:
        return f"{type(self).__name__}(scale={self.scale}, name={self.name}, abbr={self.abbr})"

    def __str__(self) -> str:
        return self.abbr

    def __lt__(self, other) -> bool:
        """
        :type other: SIPrefix
        :raise TypeError:
        """
        if not isinstance(other, SIPrefix):
            raise TypeError

        return self.scale < other.scale

    def __eq__(self, other) -> bool:
        """
        :type other: SIPrefix
        :raise TypeError:
        """
        if not isinstance(other, SIPrefix):
            raise TypeError

        return self.scale == other.scale

    def __gt__(self, other) -> bool:
        """
        :type other: SIPrefix
        :raise TypeError:
        """
        if not isinstance(other, SIPrefix):
            raise TypeError

        return self.scale > other.scale

    def __mul__(self, other):
        """
        :param other:
        :rtype: SIPrefix | int | float
        :raise TypeError:
        """
        if isinstance(other, SIPrefix):
            return SIPrefix(self.scale * other.scale)
        elif isinstance(other, (int, float)):
            return self.scale * other
        else:
            raise TypeError

    def __truediv__(self, other):
        """
        :param other:
        :rtype: SIPrefix | int | float
        :raise TypeError:
        """
        if isinstance(other, SIPrefix):
            return SIPrefix(self.scale / other.scale)
        elif isinstance(other, (int, float)):
            return self.scale / other
        else:
            raise TypeError

    def __floordiv__(self, other):
        """
        :param other:
        :rtype: SIPrefix | int | float
        :raise TypeError:
        """
        if isinstance(other, SIPrefix):
            return SIPrefix(self.scale // other.scale)
        elif isinstance(other, (int, float)):
            return self.scale // other
        else:
            raise TypeError

    def __mod__(self, other):
        """
        :param other:
        :rtype: SIPrefix | int | float
        :raise TypeError:
        """
        if isinstance(other, SIPrefix):
            return SIPrefix(self.scale % other.scale)
        elif isinstance(other, (int, float)):
            return self.scale % other
        else:
            raise TypeError

    def __pow__(self, power: int, modulo: typing.Optional[int] = None):
        """
        :rtype: SIPrefix
        :raise TypeError:
        """
        if not isinstance(power, int):
            raise TypeError

        return type(self)(self.scale ** power)

    @property
    def scale(self) -> Decimal:
        """

        :return:
        """
        return self._scale

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

        return type(name, (cls,), {"__init__": __init__})


Yotta = SIPrefix.factory("Yotta", Decimal("1E+24"), "yotta", "Y")
Zetta = SIPrefix.factory("Zetta", Decimal("1E+21"), "zetta", "Z")
Exa = SIPrefix.factory("Exa", Decimal("1E+18"), "exa", "E")
Peta = SIPrefix.factory("Peta", Decimal("1E+15"), "peta", "P")
Tera = SIPrefix.factory("Tera", Decimal("1E+12"), "tera", "T")
Giga = SIPrefix.factory("Giga", Decimal("1E+9"), "giga", "G")
Mega = SIPrefix.factory("Mega", Decimal("1E+6"), "mega", "M")
Kilo = SIPrefix.factory("Kilo", Decimal("1E+3"), "kilo", "k")
Hecto = SIPrefix.factory("Hecto", Decimal("1E+2"), "hecto", "h")
Deka = SIPrefix.factory("Deka", Decimal("1E+1"), "deka", "da")
Deci = SIPrefix.factory("Deci", Decimal("1E-1"), "deci", "d")
Centi = SIPrefix.factory("Centi", Decimal("1E-2"), "centi", "c")
Milli = SIPrefix.factory("Milli", Decimal("1E-3"), "milli", "m")
Micro = SIPrefix.factory("Micro", Decimal("1E-6"), "micro", "μ")
Nano = SIPrefix.factory("Nano", Decimal("1E-9"), "nano", "n")
Pico = SIPrefix.factory("Pico", Decimal("1E-12"), "pico", "p")
Femto = SIPrefix.factory("Femto", Decimal("1E-15"), "femto", "f")
Atto = SIPrefix.factory("Atto", Decimal("1E-18"), "atoo", "a")
Zepto = SIPrefix.factory("Zepto", Decimal("1E-21"), "zepto", "z")
Yocto = SIPrefix.factory("Yocto", Decimal("1E-24"), "yocto", "y")
