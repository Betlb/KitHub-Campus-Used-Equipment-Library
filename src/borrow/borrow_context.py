# src/borrow/borrow_context.py

class BorrowContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def borrow(self, user, equipment):
        if not self.strategy.is_eligible(user, equipment):
            raise Exception("Not eligible to borrow this item.")

        # This is the key change. We are no longer returning a simple dictionary.
        # Instead, we will create a BorrowRequest in the database.
        # We need access to the db and the BorrowRequest model.
        from .db import db
        from .models import BorrowRequest

        # Create a new borrow request with a 'pending' status.
        # The equipment status does NOT change to 'borrowed' yet.
        new_request = BorrowRequest(
            user_id=user.id,
            equipment_id=equipment.id,
            status="pending",  # <-- The request is now an offer
            # You might want to calculate and store dates here too
            # start_date=...,
            # end_date=...,
        )
        db.session.add(new_request)
        db.session.commit()
        
        # We return the request object itself.
        return new_request