from flask import Blueprint, render_template, request, redirect, url_for
from .borrow_context import BorrowContext
from .borrow_strategy import StandardBorrowStrategy
from .models import User, Equipment

borrow_bp = Blueprint('borrow', __name__)

# Mock database
items = [
    Equipment(1, "Camera", "media", "available"),
    Equipment(2, "Oscilloscope", "lab", "borrowed"),
]

@borrow_bp.route('/catalog')
def catalog():
    return render_template('catalog.html', items=items)

@borrow_bp.route('/borrow/<int:item_id>', methods=['GET', 'POST'])
def borrow_form(item_id):
    item = next((i for i in items if i.id == item_id), None)
    if request.method == 'POST':
        user = User(1, "Alice", "student")
        strategy = StandardBorrowStrategy()
        context = BorrowContext(strategy)
        try:
            context.borrow(user, item)
            return redirect(url_for('borrow.confirmation'))
        except Exception as e:
            return render_template('borrow_form.html', item=item, error=str(e))
    return render_template('borrow_form.html', item=item)

@borrow_bp.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
