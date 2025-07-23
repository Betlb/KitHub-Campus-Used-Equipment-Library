class BorrowContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def borrow(self, user, equipment):
        if not self.strategy.is_eligible(user, equipment):
            raise Exception("Not eligible to borrow this item.")
        return {"duration": self.strategy.get_max_duration()}

