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

class ClubBorrowStrategy(BorrowStrategy):
    def is_eligible(self, user, equipment):
        return equipment.status == 'available' and user.role == 'club'

    def get_max_duration(self):
        return 14

def get_strategy_for_user(user):
    if user.role == 'club':
        return ClubBorrowStrategy()
    elif user.role == 'student':
        return StandardBorrowStrategy()
    else:
        raise Exception("Borrowing not supported for this user role.")
