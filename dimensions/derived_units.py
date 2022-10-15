"""

"""

import typing

from .base_units import BaseUnit


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
        return f"{type(self).__name__}({self.sequence}"

    def __eq__(self, other) -> bool:
        """
        :type other: UnitSequence
        :raise TypeError:
        """
        if not isinstance(other, type(self)):
            raise TypeError

        return self.sequence == other.sequence

    def __bool__(self) -> bool:
        return bool(self.sequence)

    def __len__(self) -> int:
        return len(self.sequence)

    def __getitem__(self, item: int) -> BaseUnit:
        return self.sequence[item]

    def __iter__(self) -> typing.Iterable:
        return self.sequence

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
                return type(self)()
            else:
                raise ValueError
        else:
            raise TypeError

    def __floordiv__(self, other):
        """
        :type other: UnitSequence
        :rtype: UnitSequence
        :raise TypeError:
        """
        if not isinstance(other, type(self)):
            raise TypeError

        return type(self)(*filter(lambda x: x in other.sequence, self.sequence))

    def __mod__(self, other):
        """
        :type other: UnitSequence
        :rtype: UnitSequence
        :raise TypeError:
        """
        if not isinstance(other, type(self)):
            raise TypeError

        return type(self)(*filter(lambda x: x not in other.sequence, self.sequence))

    @property
    def sequence(self) -> typing.List[BaseUnit]:
        """

        :return:
        """
        return self._sequence