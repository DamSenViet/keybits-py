from ..validatable import Validatable
from .point import Point

class Line(Validatable):
  self._start = Point()
  self._end = Point()


# line segment intersection algorithm
# https://stackoverflow.com/a/60368757/8625882