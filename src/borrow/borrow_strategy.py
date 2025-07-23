class BorrowStrategy:
    def is_eligible(self, user, equipment):
        raise NotImplementedError

    def get_max_duration(self):
        raise NotImplementedError

class StandardBorrowStrategy(BorrowStrategy):
    def is_eligible(self, user, equipment):
        return equipment.status == 'available' and user.role == 'student'

    def get_max_duration(self):
        return 7
