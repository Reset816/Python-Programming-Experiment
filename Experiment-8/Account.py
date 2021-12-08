import pickle
from Transaction import Transaction


class Account:
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "James Bound")
    >>> t = Transaction(200, "2021-12-07")
    >>> account.apply(t)
    >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
    >>> account.apply(t)
    >>> account.save()
    >>> account2 = Account(name, "James Bound")
    >>> account2.load()
    >>> account2.balance
    208.0
    >>> os.remove(name + ".acc")
    """

    def __init__(self, no, name):
        """
        >>> account = Account(12, "James Bound")
        >>> account.no, account.name
        (12, 'James Bound')
        """
        assert len(name) >= 4

        self.__no = no
        self.__name = name
        self.transactions = []

    @property
    def no(self):
        return self.__no

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __len__(self):
        """
        >>> account = Account(12, "James Bound")
        >>> t = Transaction(200, "2021-12-07")
        >>> account.apply(t)
        >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
        >>> account.apply(t)
        >>> len(account)
        2
        """
        return len(self.transactions)

    @property
    def balance(self):
        count = 0
        for transaction in self.transactions:
            count += transaction.usd
        return count

    @property
    def all_usd(self):
        for transaction in self.transactions:
            if transaction.currency != "USD":
                return False
        return True

    def save(self):
        """
        >>> account = Account(12, "James Bound")
        >>> t = Transaction(200, "2021-12-07")
        >>> account.apply(t)
        >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
        >>> account.apply(t)
        >>> account.save()
        """
        file_name = str(self.no) + ".acc"
        with open(file_name, "wb") as f:
            pickle.dump(self, f)

    def load(self):
        """
        >>> account = Account(12, "James Bound")
        >>> t = Transaction(200, "2021-12-07")
        >>> account.apply(t)
        >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
        >>> account.apply(t)
        >>> account.save()
        >>> account2 = Account(12, "James Bound")
        >>> account2.load()
        >>> account2.balance
        208.0
        """
        file_name = str(self.no) + ".acc"
        with open(file_name, "rb") as f:
            tmp = pickle.load(f)
        for item in tmp.transactions:
            self.transactions.append(item)

    def apply(self, transaction):
        """
        >>> account = Account(12, "James Bound")
        >>> t = Transaction(200, "2021-12-07")
        >>> account.apply(t)
        >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
        >>> account.apply(t)
        >>> account.all_usd
        False
        >>> account.balance
        208.0
        """
        self.transactions.append(transaction)


if __name__ == "__main__":

    import doctest

    doctest.testmod()
