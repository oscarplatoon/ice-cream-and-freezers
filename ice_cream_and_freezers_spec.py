import unittest
from ice_cream import IceCream
from freezer import Freezer


class TestIceCreamAndFreezers(unittest.TestCase):
    # Go ahead and write some tests here for your code. We know that you'll at least need the IceCream and Freezer class.
    def setUp(self):
       self.freezer = Freezer()
       self.chocolate = IceCream('chocolate')
       self.peanut_butter = IceCream('Peanut Butter', 'h')
    
    def test_one_insert_icecream(self):
        self.freezer.insert_ice_cream(self.chocolate)
        self.freezer.insert_ice_cream(self.peanut_butter)
        self.assertEqual(self.freezer.get_ice_cream(), [("chocolate", 'watery'), ("Peanut Butter", "watery")])

    def test_remove_icecream(self):
        self.freezer.insert_ice_cream(self.chocolate)
        print(self.freezer)
        self.freezer.remove_ice(self.chocolate)
        print(self.freezer)
        self.assertEqual(self.freezer.storage, [])
    
    def test_update_status(self):
        self.freezer.insert_ice_cream(self.chocolate)
        self.freezer.insert_ice_cream(self.peanut_butter)
        for ice in self.freezer.storage:
            ice.set_time_in_freeze(6)
            ice.update_status()
        self.assertEqual(self.freezer.get_ice_cream(), [("chocolate", 'freezer_burned'), ("Peanut Butter", "almost_ready")])

if __name__ == '__main__':
    unittest.main()
