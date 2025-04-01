from main.IMoney import IMoney

class MoneyBag(IMoney):
    """
    A MoneyBag defers exchange rate conversions. For example, adding
    12 Swiss Francs to 14 US Dollars is represented as a bag
    containing the two Monies 12 CHF and 14 USD. Adding another
    10 Swiss francs gives a bag with 22 CHF and 14 USD. Due to
    the deferred exchange rate conversion, we can later value a
    MoneyBag with different exchange rates.
    """

    def __init__(self):
        """
        Constructs an empty MoneyBag.
        """
        self._monies = []

    @staticmethod
    def create(m1, m2):
        """
        Creates a MoneyBag containing two IMoney objects.
        """
        result = MoneyBag()
        m1.append_to(result)
        m2.append_to(result)
        return result.simplify()

    def add(self, m):
        """
        Adds a money to this MoneyBag.
        """
        return m.add_money_bag(self)

    def add_money(self, m):
        """
        Adds a Money to this MoneyBag.
        """
        return MoneyBag.create(m, self)

    def add_money_bag(self, s):
        """
        Adds another MoneyBag to this MoneyBag.
        """
        return MoneyBag.create(s, self)

    def append_bag(self, a_bag):
        """
        Appends all monies from another MoneyBag to this MoneyBag.
        """
        for money in a_bag._monies:
            self.append_money(money)

    def append_money(self, a_money):
        """
        Appends a Money to this MoneyBag.
        """
        if a_money.is_zero():
            return
        old = self.find_money(a_money.currency())
        if old is None:
            self._monies.append(a_money)
        else:
            self._monies.remove(old)
            sum_money = old.add(a_money)
            if not sum_money.is_zero():
                self._monies.append(sum_money)

    def __eq__(self, other):
        """
        Checks equality between this MoneyBag and another object.
        """
        if self.is_zero() and isinstance(other, IMoney):
            return other.is_zero()

        if isinstance(other, MoneyBag):
            if len(other._monies) != len(self._monies):
                return False
            for money in self._monies:
                if not other.contains(money):
                    return False
            return True
        return False

    def find_money(self, currency):
        """
        Finds a Money in this MoneyBag by its currency.
        """
        for money in self._monies:
            if money.currency() == currency:
                return money
        return None

    def contains(self, m):
        """
        Checks if this MoneyBag contains a specific Money.
        """
        found = self.find_money(m.currency())
        return found is not None and found.amount() == m.amount()

    def __hash__(self):
        """
        Returns the hash code for this MoneyBag.
        """
        return sum(hash(money) for money in self._monies)

    def is_zero(self):
        """
        Checks if this MoneyBag is empty or contains only zero values.
        """
        return len(self._monies) == 0

    def multiply(self, factor):
        """
        Multiplies all monies in this MoneyBag by a given factor.
        """
        result = MoneyBag()
        if factor != 0:
            for money in self._monies:
                result.append_money(money.multiply(factor))
        return result

    def negate(self):
        """
        Negates all monies in this MoneyBag.
        """
        result = MoneyBag()
        for money in self._monies:
            result.append_money(money.negate())
        return result

    def simplify(self):
        """
        Simplifies this MoneyBag. If it contains only one Money, return it.
        """
        if len(self._monies) == 1:
            return self._monies[0]
        return self

    def subtract(self, m):
        """
        Subtracts a money from this MoneyBag.
        """
        return self.add(m.negate())

    def __str__(self):
        """
        Returns a string representation of this MoneyBag.
        """
        return "{" + ", ".join(str(money) for money in self._monies) + "}"

    def append_to(self, m):
        """
        Appends this MoneyBag to another MoneyBag.
        """
        m.append_bag(self)