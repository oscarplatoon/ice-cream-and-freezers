import unittest
from modules.ice_cream import IceCream
from modules.freezer import Freezer

class TestIceCream(unittest.TestCase):
    def setUp(self):
        self.test_icecream = IceCream("Vanilla")

    def test_flavor(self):
        self.assertTrue(self.test_icecream.get_flavor, "Vanilla")

    def test_set_freezer_cycle(self):
        self.test_icecream.set_freezer_cycles(1)
        self.assertTrue(self.test_icecream.get_freezer_cycles, 1)

    def test_return_status_butter(self):
        self.test_icecream.freezer_cycles = 6
        self.assertTrue(self.test_icecream.return_status(), "over_churned")
        self.test_icecream.freezer_cycles = 10
        self.assertTrue(self.test_icecream.return_status(), "butter")

class TestFreezer(unittest.TestCase):
    def setUp(self):
        self.test_freezer = Freezer()
        self.test_freezer.store_ice_cream("Peanut Butter")
        self.test_freezer.store_ice_cream("Vanilla")

    def test_freezer_exists(self):
        self.assertIsInstance(type(self.test_freezer), object)

    def test_freezer_cycle(self):
        self.test_freezer.freeze_ice_cream()
        self.assertTrue(self.test_freezer.storage[0].get_freezer_cycles(), 1)
        # The above is a violation of the "single ." rule. How do you OOP test suites?

    def test_freezer_remove_first(self):
        removed_ice_cream = self.test_freezer.remove_first_ice_cream()
        self.assertTrue(removed_ice_cream.flavor, "Vanilla")
        self.assertTrue(len(self.test_freezer.storage), 1)

    # Test Empty Freezer Exception:
    def test_empty_freezer(self):
        self.test_freezer.remove_first_ice_cream()
        self.test_freezer.remove_first_ice_cream()
        with self.assertRaises(Exception) as context:
            self.test_freezer.remove_first_ice_cream()
        self.assertEqual("Freezer is Empty.", str(context.exception))
    
    # Test too full:
    def test_full_freezer(self):
        self.test_freezer.size = 2
        with self.assertRaises(Exception) as context:
            self.test_freezer.store_ice_cream("Chocolate")
        self.assertEqual("The freezer is full!", str(context.exception))

    def test_remove_by_doneness(self):
        # We should test that it's returning what we're asking
        # We should test that it has actually removed an item from freezer storage
        # WIP Refactor this test to use the freezer doneness_check:
        removed_ice_cream = self.test_freezer.remove_ice_cream_by_status("Peanut Butter", "watery")
        self.assertTrue(removed_ice_cream.flavor, "Peanut Butter")
        self.assertTrue(len(self.test_freezer.storage), 1)

class TestAgingIceCream(unittest.TestCase):
    def setUp(self):
        self.test_freezer = Freezer()
        self.test_freezer.store_ice_cream("Peanut Butter")
        self.test_freezer.store_ice_cream("Vanilla")
        self.test_freezer.store_ice_cream("Chocolate")
        self.test_freezer.store_ice_cream("Strawberry")

    def test_freezer_aging(self):
        self.test_freezer.freeze_ice_cream()
        for ice_cream in self.test_freezer.storage:
            self.assertTrue(ice_cream.get_freezer_cycles(), 1)

    def test_freezer_remove_aged_by_status(self):
        self.test_freezer.freeze_ice_cream()
        with self.assertRaises(Exception) as context:
            self.test_freezer.remove_ice_cream_by_status("Peanut Butter", "watery")
        self.assertTrue("ice cream you're looking for" in str(context.exception))

    def test_repeat_cycle_icecream_and_remove(self):
        #Age icecream to freezer cycles 4:
        self.test_freezer.freeze_ice_cream()
        self.test_freezer.freeze_ice_cream()
        self.test_freezer.freeze_ice_cream()
        self.test_freezer.freeze_ice_cream()
        #Pull "ready" Strawberry Icecream
        removed_ice_cream = self.test_freezer.remove_ice_cream_by_status("Strawberry", "ready")
        self.assertTrue(removed_ice_cream.flavor, "Strawberry")

if __name__ == '__main__':
    unittest.main()
