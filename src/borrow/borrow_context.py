# src/borrow/borrow_context.py

class BorrowContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def borrow(self, user, equipment):
        if not self.strategy.is_eligible(user, equipment):
            raise Exception("Not eligible to borrow this item.")

        from .db import db
        from .models import BorrowRequest

        new_request = BorrowRequest(
            user_id=user.id,
            equipment_id=equipment.id,
            status="pending",
        )
        db.session.add(new_request)
        db.session.commit()
        
        return new_request