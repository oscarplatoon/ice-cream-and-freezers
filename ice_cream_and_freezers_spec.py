import unittest
from ice_cream import IceCream
from freezer import Freezer

class TestIceCream(unittest.TestCase):
    def setUp(self):
        self.test_icecream = IceCream("Vanilla")

    def test_flavor(self):
        self.assertTrue(self.test_icecream.get_flavor, "Vanilla")

    def test_set_done_status(self):
        self.test_icecream.set_done_status("Butter")
        self.assertTrue(self.test_icecream.get_done_status, "Butter")

class TestFreezer(unittest.TestCase):
    def setUp(self):
        pass
    pass

if __name__ == '__main__':
    unittest.main()
