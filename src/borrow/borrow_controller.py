from flask import Blueprint, render_template, request, redirect, url_for, flash
from .borrow_context import BorrowContext
from .borrow_strategy import StandardBorrowStrategy
from .models import User, Equipment, BorrowRequest
from datetime import datetime, timedelta
from .db import db

borrow_bp = Blueprint('borrow', __name__)

@borrow_bp.route('/catalog')
def catalog():
    items = Equipment.query.all()
    return render_template('catalog.html', items=items)

@borrow_bp.route('/borrow/<int:item_id>', methods=['GET', 'POST'])
def borrow_form(item_id):
    item = Equipment.query.get(item_id)
    if request.method == 'POST':
        user = User.query.get(1)  # mock login
        strategy = StandardBorrowStrategy()
        context = BorrowContext(strategy)
        try:
            context.borrow(user, item)

            # ✅ Store BorrowRequest in DB
            borrow_request = BorrowRequest(
                user_id=user.id,
                equipment_id=item.id,
                start_date=datetime.now().strftime('%Y-%m-%d'),
                end_date=(datetime.now() + timedelta(days=strategy.get_max_duration())).strftime('%Y-%m-%d'),
                status="pending",
                notes=request.form.get("notes", "")
            )
            item.status = "borrowed"
            db.session.add(borrow_request)
            db.session.commit()

            flash("Borrow request submitted!", "success")
            return redirect(url_for('borrow.confirmation'))

        except Exception as e:
            return render_template('borrow_form.html', item=item, error=str(e))

    return render_template('borrow_form.html', item=item)

@borrow_bp.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
