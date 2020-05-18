from decimal import (
    Decimal,
    getcontext
)
from ..validatable import Validatable

# default mathjs precision
getcontext().prec = 64
class Point(Validatable):
    def __init__(self, options):
        pass
