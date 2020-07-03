from decimal import (
    Decimal,
    getcontext
)
from ..validatable import Validatable

# default mathjs precision
getcontext().prec = 64
class Point(Validatable):
    def __init__(self, x: float = 0, y: float = 0):
        if type(x) == float and type(y) == float:
            self._x = Decimal(x)
            self._y = Decimal(y)
        else:
            raise TypeError("Only numbers allowed!")
    def get_x(self, val: float):
        return self._x
    def get_y(self, val: float):
        return self._y
    def set_x(self, val: float):
        if type(val) == float:
            self._x = Decimal(val)
        else:
            raise TypeError("Only numbers allowed!")
    def set_y(self, val: float):
        if type(val) == float:
            self._y = Decimal(val)
        else:
            raise TypeError("Only numbers allowed!")
    def equals(self, val: Point):
        return True if self._x == val.get_x() and self._y == val.get_y() else False

    # TODO converting to and from JSON
    def fromJSON(self):
        pass
    def toJSON(self):
        pass