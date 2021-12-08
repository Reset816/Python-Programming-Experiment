#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:
    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    def __add__(self, other):
        """将两点的坐标相加
        >>> p = Point(6, 7)
        >>> q = p + Point(1, 2)
        >>> q
        Point(7, 9)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """将另一个点的坐标加到该点上
        >>> p = Point(4, 1)
        >>> p += Point(2, 0)
        >>> p
        Point(6, 1)
        """
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        """将两点的坐标相减
        >>> p = Point(1, 9)
        >>> q = p - Point(-1, 1)
        >>> q
        Point(2, 8)
        """
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """将另一个点的坐标减到该点上
        >>> p = Point(1, 9)
        >>> p -= Point(-1, 1)
        >>> p
        Point(2, 8)
        """
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        """将该点坐标乘以一个数
        >>> p = Point(1, 3)
        >>> q = p * 2
        >>> q
        Point(2, 6)
        """
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        """将该点坐标等于该点坐标乘以一个数
        >>> p = Point(1, 3)
        >>> p *= 2
        >>> p
        Point(2, 6)
        """
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other):
        """将该点坐标除以一个数
        >>> p = Point(6, 4)
        >>> q = p / 2
        >>> q
        Point(3.0, 2.0)
        """
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        """将该点坐标等于该点坐标除以一个数
        >>> p = Point(6, 4)
        >>> p /= 2
        >>> p
        Point(3.0, 2.0)
        """
        self.x /= other
        self.y /= other
        return self

    def __floordiv__(self, other):
        """将该点坐标除以一个数并向下取整
        >>> p = Point(7, 4)
        >>> q = p // 2
        >>> q
        Point(3, 2)
        """
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        """将该点坐标等于该点坐标除以一个数并向下取整
        >>> p = Point(7, 4)
        >>> p //= 2
        >>> p
        Point(3, 2)
        """
        self.x //= other
        self.y //= other
        return self


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
