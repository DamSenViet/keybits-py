from __future__ import annotations
from decimal import (
    Decimal,
    getcontext
)
# default mathjs precision
getcontext().prec = 64


class Point:
    """Immutable Point
    """

    def __init__(self) -> None:
        """Instantiates a Point.
        """
        pass

    def equals(self, point: Point) -> bool:
        """Determines whether invoking Point is equivalent to passed Point.

        Args:
            point (Point): The Point to compare against

        Returns:
            bool: Whether the Lines are equal representations
        """
        pass
