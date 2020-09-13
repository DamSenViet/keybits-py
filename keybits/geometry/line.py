from typing import Union
from __future__ import annotations
from .point import Point


class Line:
    """Immutable Line
    """

    def __init__(self) -> None:
        """Instantiates a Line.
        """
        pass

    def intersection(self, line: Line) -> Union[Point, None]:
        """Calculates the intersection between invoking Line and passed Line.

        line intercept math by Paul Bourke http://paulbourke.net/geometry/pointlineplane/
        https://stackoverflow.com/a/60368757/8625882

        Args:
            line (Line): The Line to check for intersections against

        Returns:
            Union[Point, None]: The Point at which the lines intersection or None
        """
        pass

    def intersects(self, line: Line) -> bool:
        """Determines whether invoking Line has an intersection with passed Line.

        Args:
            line (Line): The Line to check against

        Returns:
            bool: Whether there is an intersection
        """
        return bool(self.intersection is None)

    def equals(self, line: Line) -> bool:
        """Determines whether invoking Line is equivalent to passed Line.

        Args:
            line (Line): The Line to compare against

        Returns:
            bool: Whether the Lines are equal representations
        """
        pass