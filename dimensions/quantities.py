"""

"""

from decimal import Decimal
import math
import typing

from .base_units import BaseUnit
from .derived_units import Unit


class SIQuantity:
    """

    """
    def __init__(
            self,
            magnitude: typing.Union[int, float, Decimal], unit: Unit
    ):
        """

        :param magnitude:
        """
        self._magnitude = Decimal(magnitude)
        self._unit = unit

    def __repr__(self) -> str:
        return f"{type(self).__name__}(magnitude={self.magnitude}, unit={self.unit})"

    def __str__(self) -> str:
        return f"{self.magnitude} {self.unit}"

    def __eq__(self, other) -> bool:
        """
        :type other: BaseUnit
        :raise TypeError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        return (self.magnitude == other.magnitude) and (self.unit == other.unit)

    def __bool__(self, other) -> bool:
        return bool(self.magnitude) and bool(self.unit)

    def __add__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        :raise ValueError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        if self.unit != other.unit:
            raise ValueError

        return SIQuantity(self.magnitude + other.magnitude, self.unit)

    def __iadd__(self, other):
        """
        :type other: SIQuantity
        :raise TypeError:
        :raise ValueError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        if self.unit != other.unit:
            raise ValueError

        self.__init__(self.magnitude + other.magnitude, self.unit)

    def __sub__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        :raise ValueError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        if self.unit != other.unit:
            raise ValueError

        return SIQuantity(self.magnitude - other.magnitude, self.unit)

    def __isub__(self, other):
        """
        :type other: SIQuantity
        :raise TypeError:
        :raise ValueError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        if self.unit != other.unit:
            raise ValueError

        self.__init__(self.magnitude - other.magnitude, self.unit)

    def __mul__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        return SIQuantity(self.magnitude * other.magnitude, self.unit * other.unit)

    def __imul__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        self.__init__(self.magnitude * other.magnitude, self.unit * other.unit)

    def __truediv__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        return SIQuantity(self.magnitude / other.magnitude, self.unit / other.unit)

    def __itruediv__(self, other):
        """
        :type other: SIQuantity
        :rtype: SIQuantity
        :raise TypeError:
        """
        if not isinstance(other, SIQuantity):
            raise TypeError

        self.__init__(self.magnitude / other.magnitude, self.unit / other.unit)

    def __pow__(self, power: int, modulo: typing.Optional[int] = None):
        """
        :rtype: SIQuantity
        """
        if not isinstance(power, int):
            raise TypeError

        return SIQuantity(self.magnitude ** power, self.unit ** power)

    def __ipow__(self, power: int, modulo: typing.Optional[int] = None):
        """
        :rtype: SIQuantity
        """
        if not isinstance(power, int):
            raise TypeError

        self.__init__(self.magnitude ** power, self.unit ** power)

    def __neg__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(-self.magnitude, self.unit)

    def __pos__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(self.magnitude, self.unit)

    def __abs__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(abs(self.magnitude), self.unit)

    def __int__(self) -> int:
        return int(self.magnitude)

    def __float__(self) -> float:
        return float(self.magnitude)

    def __round__(self, ndigits: typing.Optional[int] = None):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(round(self.magnitude, ndigits), self.unit)

    def __trunc__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(math.trunc(self.magnitude), self.unit)

    def __floor__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(math.floor(self.magnitude), self.unit)

    def __ceil__(self):
        """
        :rtype: SIQuantity
        """
        return SIQuantity(math.ceil(self.magnitude), self.unit)

    @property
    def magnitude(self) -> Decimal:
        """

        :return:
        """
        return self._magnitude

    @property
    def unit(self) -> Unit:
        """

        :return:
        """
        return self._unit
