import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.Money import Money
from main.MoneyBag import MoneyBag


class TestMoney(unittest.TestCase):
    def test_add(self):
        ten_euro = Money(10, "EURO")
        self.assertEqual(10, ten_euro.amount())
        self.assertEqual("EURO", ten_euro.currency())

    def test_negative_amount(self):
        negative_money = Money(-5, "USD")
        self.assertEqual(-5, negative_money.amount())

    def test_zero_amount(self):
        zero_money = Money(0, "USD")
        self.assertEqual(0, zero_money.amount())
        self.assertTrue(zero_money.is_zero())

    def test_different_currencies_not_equal(self):
        usd = Money(10, "USD")
        eur = Money(10, "EUR")
        self.assertNotEqual(usd, eur)

    def test_hash_code_consistency(self):
        money1 = Money(10, "USD")
        money2 = Money(10, "USD")
        self.assertEqual(hash(money1), hash(money2))

    def test_equals_with_imoney(self):
        zero_money = Money(0, "USD")
        mock_imoney = Money(0, "USD")
        self.assertEqual(zero_money, mock_imoney)

    def test_equals_with_non_imoney_object(self):
        zero_money = Money(0, "USD")
        non_imoney_object = object()
        self.assertNotEqual(zero_money, non_imoney_object)

    def test_equals_with_imoney_when_zero(self):
        zero_money = Money(0, "USD")
        another_zero_money = Money(0, "USD")
        self.assertEqual(zero_money, another_zero_money)

    def test_add_money(self):
        ten_euro = Money(10, "EURO")
        five_euro = Money(5, "EURO")
        result = ten_euro.add_money(five_euro)
        self.assertEqual(Money(15, "EURO"), result)

        ten_usd = Money(10, "USD")
        result = ten_euro.add_money(ten_usd)
        expected = MoneyBag.create(ten_euro, ten_usd)
        self.assertEqual(expected, result)

    def test_add_money_bag(self):
        ten_euro = Money(10, "EURO")
        bag = MoneyBag.create(Money(5, "USD"), Money(15, "EURO"))
        result = ten_euro.add_money_bag(bag)
        expected = MoneyBag.create(Money(25, "EURO"), Money(5, "USD"))
        self.assertEqual(expected, result)

    def test_amount(self):
        ten_euro = Money(10, "EURO")
        self.assertEqual(10, ten_euro.amount())

    def test_currency(self):
        ten_euro = Money(10, "EURO")
        self.assertEqual("EURO", ten_euro.currency())

    def test_equals(self):
        ten_euro = Money(10, "EURO")
        self.assertEqual(ten_euro, ten_euro)

        another_ten_euro = Money(10, "EURO")
        self.assertEqual(ten_euro, another_ten_euro)

        five_euro = Money(5, "EURO")
        self.assertNotEqual(ten_euro, five_euro)

        ten_usd = Money(10, "USD")
        self.assertNotEqual(ten_euro, ten_usd)

        self.assertNotEqual(ten_euro, None)
        self.assertNotEqual(ten_euro, "string")

    def test_hash_code(self):
        ten_euro = Money(10, "EURO")
        another_ten_euro = Money(10, "EURO")
        self.assertEqual(hash(ten_euro), hash(another_ten_euro))

    def test_is_zero(self):
        zero_euro = Money(0, "EURO")
        self.assertTrue(zero_euro.is_zero())

        ten_euro = Money(10, "EURO")
        self.assertFalse(ten_euro.is_zero())

    def test_multiply(self):
        ten_euro = Money(10, "EURO")
        result = ten_euro.multiply(2)
        self.assertEqual(Money(20, "EURO"), result)

        result = ten_euro.multiply(0)
        self.assertEqual(Money(0, "EURO"), result)

        result = ten_euro.multiply(-2)
        self.assertEqual(Money(-20, "EURO"), result)

    def test_negate(self):
        ten_euro = Money(10, "EURO")
        result = ten_euro.negate()
        self.assertEqual(Money(-10, "EURO"), result)

        zero_euro = Money(0, "EURO")
        result = zero_euro.negate()
        self.assertEqual(Money(0, "EURO"), result)

        negative_euro = Money(-10, "EURO")
        result = negative_euro.negate()
        self.assertEqual(Money(10, "EURO"), result)

    def test_subtract(self):
        ten_euro = Money(10, "EURO")
        five_euro = Money(5, "EURO")
        result = ten_euro.subtract(five_euro)
        self.assertEqual(Money(5, "EURO"), result)

        zero_euro = Money(0, "EURO")
        result = ten_euro.subtract(zero_euro)
        self.assertEqual(Money(10, "EURO"), result)

        negative_euro = Money(-5, "EURO")
        result = ten_euro.subtract(negative_euro)
        self.assertEqual(Money(15, "EURO"), result)

    def test_to_string(self):
        ten_euro = Money(10, "EURO")
        self.assertEqual("[10 EURO]", str(ten_euro))


if __name__ == "__main__":
    unittest.main()