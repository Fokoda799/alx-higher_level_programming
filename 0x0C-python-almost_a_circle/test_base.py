#!/usr/bin/python3
"""test_base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_default_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_custom_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_no_num_id(self):
        b = Base('a')

if __name__ == '__main__':
    unittest.main()
