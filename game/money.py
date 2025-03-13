class MoneyCard:
    def __init__(self, amount: int):
        assert amount in [0, 10, 50, 100, 200, 500], "Invalid amount"
        self.amount = amount
