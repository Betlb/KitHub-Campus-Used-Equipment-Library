from .db import db
from .models import BorrowRequest
from datetime import datetime, timedelta

class BorrowContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def borrow(self, user, equipment, notes="", start_date=None, end_date=None):
        if not self.strategy.is_eligible(user, equipment):
            raise Exception("Not eligible to borrow this item.")

        start_date = start_date or datetime.now().strftime('%Y-%m-%d')
        end_date = end_date or (datetime.now() + timedelta(days=self.strategy.get_max_duration())).strftime('%Y-%m-%d')

        new_request = BorrowRequest(
            user_id=user.id,
            equipment_id=equipment.id,
            status="pending",
            start_date=start_date,
            end_date=end_date,
            notes=notes
        )
        db.session.add(new_request)
        db.session.commit()

        return new_request
