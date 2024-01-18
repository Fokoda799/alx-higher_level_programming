#!/usr/bin/python3
"""the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Privet attrs"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return square reprisntion"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
