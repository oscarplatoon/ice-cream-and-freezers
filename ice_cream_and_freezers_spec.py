import unittest
from ice_cream_and_freezers import IceCream, Freezer


class TestIceCreamAndFreezers(unittest.TestCase):
    def setUp(self):
        self.frzr = Freezer()
        self.choco = IceCream("Chocolate", 3)
        self.vanil = IceCream("Vanilla", 2)

    def test_put_ice_cream_into_freezer(self):
        self.frzr.put(self.choco)
        self.frzr.put(self.vanil)
        self.assertEqual(self.frzr.return_ice_cream(), [
                         ("Chocolate", "watery"), ("Vanilla", "watery")])

    def test_take_ice_cream_out(self):
        self.frzr.put(self.choco)
        self.frzr.put(self.vanil)
        self.frzr.remove("Chocolate")
        self.assertEqual(self.frzr.return_ice_cream(), [("Vanilla", "watery")])

    def test_freeze_ice_cream(self):
        self.frzr.put(IceCream("Chocolate", 3))
        self.frzr.put(IceCream("Vanilla", 2))
        self.frzr.freeze()
        self.frzr.freeze()
        self.assertEqual(self.frzr.return_ice_cream(), [
                         ("Chocolate", "almost_ready"), ("Vanilla", "ready")])

    def test_burn_freezer(self):
        self.frzr.put(IceCream("Chocolate", 3))
        self.frzr.put(IceCream("Vanilla", 2))
        self.frzr.freeze()
        self.frzr.freeze()
        self.frzr.freeze()
        self.frzr.freeze()
        self.assertEqual(self.frzr.return_ice_cream(), [
                         ("Chocolate", "freezer_burned"), ("Vanilla", "freezer_burned")])


if __name__ == '__main__':
    unittest.main()
