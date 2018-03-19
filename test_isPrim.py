from unittest import TestCase
from isPrim import isPrim

class TestIsPrim(TestCase):
    def test_isPrim_5(self):
        self.assertEqual(True, isPrim(5))
    def test_isPrim_4(self):
        self.assertEqual(False, isPrim(4))
    def test_isPrim_minusz_4(self):
        self.assertEqual(False, isPrim(-4))
    def test_isPrim_1(self):
        self.assertEqual(False, isPrim(1))
    def test_isPrim_0(self):
        self.assertEqual(False, isPrim(0))
    def test_isPrim_minusz_3(self):
        self.assertEqual(False, isPrim(-3))
