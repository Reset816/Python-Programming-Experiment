class Transaction:
    def __init__(
        self,
        amount,
        date,
        currency="USD",
        usd_conversion_rate=1,
        description="",
    ):
        """
        >>> t = Transaction(200, "2021-12-07")
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (200, 'USD', 1, 200)
        >>> t = Transaction(50, "2021-12-07", "CNY", 0.16)
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (50, 'CNY', 0.16, 8.0)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


if __name__ == "__main__":
    import doctest

    doctest.testmod()
