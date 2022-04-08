"""
Name: Lexie DelViscio
sphere.py

Problem: This program creates a sphere class for hw10 containing a radius, surface area,
and volume.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import pi


class Sphere:
    """
    represents a sphere with a radius, volume and surface area
    """
    def __init__(self, radius):
        """
        constructs a sphere with a radius
        """
        self.radius = radius
        self.vol = 0
        self.surf_area = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):
        self.surf_area = 4 * pi * (self.radius ** 2)
        return self.surf_area

    def volume(self):
        radius_2 = self.radius
        radius_cubed = radius_2 ** 3
        self.vol = (4/3) * pi * radius_cubed
        return self.vol
