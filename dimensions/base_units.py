"""

"""


class BaseUnit:
    """

    """
    def __init__(self, name: str, abbr: str):
        self._name = name
        self._abbr = abbr

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, abbr={self.abbr})"

    def __str__(self) -> str:
        return self.abbr

    def __eq__(self, other) -> bool:
        """

        :param other:
        :type other: BaseUnit
        :return:
        """
        if not issubclass(type(other), BaseUnit):
            raise TypeError

        return type(self) == type(other)

    @property
    def abbr(self) -> str:
        """

        :return:
        """
        return self._abbr

    @property
    def name(self) -> str:
        """

        :return:
        """
        return self._name


class Second(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("second", "s")


class Meter(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("meter", "m")


class Ampere(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("ampere", "A")


class Gram(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("gram", "g")


class Kelvin(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("kelvin", "K")


class Mole(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("mole", "mol")


class Candela(BaseUnit):
    """

    """
    def __init__(self):
        super().__init__("candela", "cd")


SECOND = Second()
METER = Meter()
AMPERE = Ampere()
GRAM = Gram()
KELVIN = Kelvin()
MOLE = Mole()
CANDELA = Candela()
