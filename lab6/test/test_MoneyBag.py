import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from main.Money import Money
from main.MoneyBag import MoneyBag
from main.IMoney import IMoney


class MoneyBagTest(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.f12CHF = Money(12, "CHF")
        self.f14CHF = Money(14, "CHF")
        self.f7USD = Money(7, "USD")
        self.f21USD = Money(21, "USD")

        self.fMB1 = MoneyBag.create(self.f12CHF, self.f7USD)
        self.fMB2 = MoneyBag.create(self.f14CHF, self.f21USD)

    def tearDown(self):
        """
        Tear down test fixtures.
        """
        str(self.fMB1)  # Ensures toString is called for testing purposes.

    def test_bag_multiply(self):
        """
        Test multiplying a MoneyBag.
        """
        expected = MoneyBag.create(Money(24, "CHF"), Money(14, "USD"))
        self.assertEqual(expected, self.fMB1.multiply(2))
        self.assertEqual(self.fMB1, self.fMB1.multiply(1))
        self.assertTrue(self.fMB1.multiply(0).is_zero())

    def test_bag_negate(self):
        """
        Test negating a MoneyBag.
        """
        expected = MoneyBag.create(Money(-12, "CHF"), Money(-7, "USD"))
        self.assertEqual(expected, self.fMB1.negate())

    def test_bag_simple_add(self):
        """
        Test adding a Money to a MoneyBag.
        """
        expected = MoneyBag.create(Money(26, "CHF"), Money(7, "USD"))
        self.assertEqual(expected, self.fMB1.add(self.f14CHF))

    def test_bag_subtract(self):
        """
        Test subtracting a MoneyBag from another MoneyBag.
        """
        expected = MoneyBag.create(Money(-2, "CHF"), Money(-14, "USD"))
        self.assertEqual(expected, self.fMB1.subtract(self.fMB2))

    def test_bag_sum_add(self):
        """
        Test adding two MoneyBags.
        """
        expected = MoneyBag.create(Money(26, "CHF"), Money(28, "USD"))
        self.assertEqual(expected, self.fMB1.add(self.fMB2))

    def test_is_zero(self):
        """
        Test if a MoneyBag is zero.
        """
        self.assertTrue(self.fMB1.subtract(self.fMB1).is_zero())
        self.assertTrue(MoneyBag.create(Money(0, "CHF"), Money(0, "USD")).is_zero())

    def test_mixed_simple_add(self):
        """
        Test adding two different currencies.
        """
        expected = MoneyBag.create(self.f12CHF, self.f7USD)
        self.assertEqual(expected, self.f12CHF.add(self.f7USD))

    def test_bag_not_equals(self):
        """
        Test inequality of MoneyBags.
        """
        bag = MoneyBag.create(self.f12CHF, self.f7USD)
        self.assertNotEqual(bag, Money(12, "DEM").add(self.f7USD))

    def test_money_bag_equals(self):
        """
        Test equality of MoneyBags.
        """
        self.assertNotEqual(self.fMB1, None)
        self.assertEqual(self.fMB1, self.fMB1)
        equal = MoneyBag.create(Money(12, "CHF"), Money(7, "USD"))
        self.assertEqual(self.fMB1, equal)
        self.assertNotEqual(self.fMB1, self.f12CHF)
        self.assertNotEqual(self.f12CHF, self.fMB1)
        self.assertNotEqual(self.fMB1, self.fMB2)

    def test_money_bag_hash(self):
        """
        Test hash codes of MoneyBags.
        """
        equal = MoneyBag.create(Money(12, "CHF"), Money(7, "USD"))
        self.assertEqual(hash(self.fMB1), hash(equal))

    def test_money_equals(self):
        """
        Test equality of Money objects.
        """
        self.assertNotEqual(self.f12CHF, None)
        equal_money = Money(12, "CHF")
        self.assertEqual(self.f12CHF, self.f12CHF)
        self.assertEqual(self.f12CHF, equal_money)
        self.assertEqual(hash(self.f12CHF), hash(equal_money))
        self.assertNotEqual(self.f12CHF, self.f14CHF)

    def test_money_hash(self):
        """
        Test hash codes of Money objects.
        """
        self.assertNotEqual(self.f12CHF, None)
        equal = Money(12, "CHF")
        self.assertEqual(hash(self.f12CHF), hash(equal))

    def test_simplify(self):
        """
        Test simplifying a MoneyBag.
        """
        money = MoneyBag.create(Money(26, "CHF"), Money(28, "CHF"))
        self.assertEqual(Money(54, "CHF"), money)

    def test_normalize2(self):
        """
        Test normalization of a MoneyBag.
        """
        expected = Money(7, "USD")
        self.assertEqual(expected, self.fMB1.subtract(self.f12CHF))

    def test_normalize3(self):
        """
        Test normalization of a MoneyBag with multiple currencies.
        """
        ms1 = MoneyBag.create(Money(12, "CHF"), Money(3, "USD"))
        expected = Money(4, "USD")
        self.assertEqual(expected, self.fMB1.subtract(ms1))

    def test_normalize4(self):
        """
        Test normalization of a MoneyBag with subtraction.
        """
        ms1 = MoneyBag.create(Money(12, "CHF"), Money(3, "USD"))
        expected = Money(-3, "USD")
        self.assertEqual(expected, self.f12CHF.subtract(ms1))

    def test_print(self):
        """
        Test string representation of Money.
        """
        self.assertEqual("[12 CHF]", str(self.f12CHF))

    def test_simple_add(self):
        """
        Test simple addition of Money objects.
        """
        expected = Money(26, "CHF")
        self.assertEqual(expected, self.f12CHF.add(self.f14CHF))

    def test_simple_bag_add(self):
        """
        Test adding a Money to a MoneyBag.
        """
        expected = MoneyBag.create(Money(26, "CHF"), Money(7, "USD"))
        self.assertEqual(expected, self.f14CHF.add(self.fMB1))

    def test_simple_multiply(self):
        """
        Test multiplying a Money object.
        """
        expected = Money(28, "CHF")
        self.assertEqual(expected, self.f14CHF.multiply(2))

    def test_simple_negate(self):
        """
        Test negating a Money object.
        """
        expected = Money(-14, "CHF")
        self.assertEqual(expected, self.f14CHF.negate())

    def test_simple_subtract(self):
        """
        Test subtracting Money objects.
        """
        expected = Money(2, "CHF")
        self.assertEqual(expected, self.f14CHF.subtract(self.f12CHF))

    def test_money_bag_equals_edge_cases(self):
        empty_bag = MoneyBag()

        # Case 1: Comparing an empty MoneyBag to itself
        self.assertTrue(empty_bag == empty_bag)

        # Case 2: Comparing an empty MoneyBag to another empty MoneyBag
        another_empty_bag = MoneyBag()
        self.assertTrue(empty_bag == another_empty_bag)

        # Case 3: Comparing an empty MoneyBag to a non-empty MoneyBag
        self.assertFalse(empty_bag == self.fMB1)

        # Case 4: Comparing MoneyBag with a Money object (should return False)
        self.assertFalse(self.fMB1 == self.f12CHF)

        # Case 5: Comparing MoneyBag to a None object
        self.assertFalse(self.fMB1 == None)

        # Case 6: Comparing MoneyBag with different sizes
        small_bag = MoneyBag.create(Money(5, "USD"), Money(10, "CHF"))
        large_bag = small_bag.add(Money(20, "EUR"))
        self.assertFalse(small_bag == large_bag)

    def test_money_bag_equals_edge_cases_2(self):
        empty_bag = MoneyBag()
        non_imoney_object = object()  # Completely unrelated object

        # Case 1: Comparing an empty MoneyBag to itself
        self.assertTrue(empty_bag == empty_bag)

        # Case 2: Comparing an empty MoneyBag to a non-IMoney object
        self.assertFalse(empty_bag == non_imoney_object)

        # Case 3: Comparing an empty MoneyBag to a non-empty MoneyBag
        self.assertFalse(empty_bag == self.fMB1)

        # Case 4: Comparing MoneyBag with a Money object (should return False)
        self.assertFalse(self.fMB1 == self.f12CHF)

        # Case 5: Comparing MoneyBag to a None object
        self.assertFalse(self.fMB1 == None)

        # Case 6: Comparing MoneyBag with different sizes
        small_bag = MoneyBag.create(Money(5, "USD"), Money(10, "CHF"))
        large_bag = small_bag.add(Money(20, "EUR"))
        self.assertFalse(small_bag == large_bag)

    def test_equals_with_non_imoney_object(self):
        money_bag = MoneyBag.create(Money(10, "USD"), Money(5, "EUR"))
        non_imoney_object = object()  # Completely unrelated object

        self.assertFalse(
            money_bag == non_imoney_object,
            "MoneyBag should not be equal to a non-IMoney object",
        )


if __name__ == "__main__":
    unittest.main()