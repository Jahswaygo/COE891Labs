from abc import ABC, abstractmethod

class IMoney(ABC):
    """
    The common interface for simple Monies and MoneyBags
    """

    @abstractmethod
    def add(self, m):
        """
        Adds a money to this money.
        """
        pass

    @abstractmethod
    def add_money(self, m):
        """
        Adds a simple Money to this money. This is a helper method for
        implementing double dispatch.
        """
        pass

    @abstractmethod
    def add_money_bag(self, s):
        """
        Adds a MoneyBag to this money. This is a helper method for
        implementing double dispatch.
        """
        pass

    @abstractmethod
    def is_zero(self):
        """
        Tests whether this money is zero.
        """
        pass

    @abstractmethod
    def multiply(self, factor):
        """
        Multiplies a money by the given factor.
        """
        pass

    @abstractmethod
    def negate(self):
        """
        Negates this money.
        """
        pass

    @abstractmethod
    def subtract(self, m):
        """
        Subtracts a money from this money.
        """
        pass

    @abstractmethod
    def append_to(self, m):
        """
        Append this to a MoneyBag m.
        """
        pass