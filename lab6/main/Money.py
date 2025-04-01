from main.IMoney import IMoney
from main.MoneyBag import MoneyBag  # Assuming MoneyBag is implemented elsewhere

class Money(IMoney):
    """
    A simple Money implementation.
    """

    def __init__(self, amount, currency):
        """
        Constructs a money object with the given amount and currency.
        """
        self._amount = amount
        self._currency = currency

    def add(self, m):
        """
        Adds a money to this money. Forwards the request to the add_money helper.
        """
        return m.add_money(self)

    def add_money(self, m):
        """
        Adds a simple Money to this money.
        """
        if m.currency() == self.currency():
            return Money(self.amount() + m.amount(), self.currency())
        return MoneyBag.create(self, m)

    def add_money_bag(self, s):
        """
        Adds a MoneyBag to this money.
        """
        return s.add_money(self)

    def amount(self):
        """
        Returns the amount of this money.
        """
        return self._amount

    def currency(self):
        """
        Returns the currency of this money.
        """
        return self._currency

    def is_zero(self):
        """
        Checks if this money is zero.
        """
        return self.amount() == 0

    def multiply(self, factor):
        """
        Multiplies this money by a given factor.
        """
        return Money(self.amount() * factor, self.currency())

    def negate(self):
        """
        Negates this money.
        """
        return Money(-self.amount(), self.currency())

    def subtract(self, m):
        """
        Subtracts a money from this money.
        """
        return self.add(m.negate())

    def append_to(self, m):
        m.append_money(self)

    def __eq__(self, other):
        if self.is_zero() and isinstance(other, IMoney):
            return other.is_zero()
        if isinstance(other, Money):
            return self.currency() == other.currency() and self.amount() == other.amount()
        return False

    def __hash__(self):
        return hash(self.currency()) + self.amount()

    def __str__(self):
        return f"[{self.amount()} {self.currency()}]"