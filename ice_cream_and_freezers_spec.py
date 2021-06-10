import unittest
from ice_cream_and_freezers import IceCream, Freezer, IceCreamMaker


class TestIceCreamAndFreezers(unittest.TestCase):
    
    def test_freezer_instantiation(self):
        tester = Freezer()
        self.assertEqual(tester.storage,[])

    def test_make_ice_cream(self):
        tester = Freezer()
        IceCreamMaker.make_ice_cream(tester,'chocolate')
        self.assertEqual(tester.storage[0].flavor,'chocolate')

    def test_state_change(self):
        tester = Freezer()
        IceCreamMaker.make_ice_cream(tester,'chocolate')
        Freezer.wait_one_hour(tester)
        self.assertEqual(tester.storage[0].state,'almost_ready')
    
    def test_check_freezer(self):
        tester = Freezer()
        IceCreamMaker.make_ice_cream(tester,'chocolate')
        Freezer.wait_one_hour(tester)
        self.assertEqual(Freezer.check_freezer(tester),f'Flavor: chocolate\tBatch: 1\tState: almost_ready')

    def test_use_ice_cream(self):
        tester = Freezer()
        IceCreamMaker.make_ice_cream(tester,'chocolate')
        Freezer.wait_one_hour(tester)
        Freezer.wait_one_hour(tester)
        self.assertEqual(IceCreamMaker.use_ice_cream(tester,'chocolate'),f"batch number 1 of chocolate is now ready. Removing now...")



if __name__ == '__main__':
    unittest.main()
