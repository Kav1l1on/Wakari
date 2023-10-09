import unittest
from sims import *

class My_Test(unittest.TestCase):

    def test_defultValue(self):
        d1 = Human()

        self.assertTrue(d1.IsAlive())
