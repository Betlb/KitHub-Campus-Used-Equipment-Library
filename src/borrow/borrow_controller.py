from flask import Blueprint, render_template, request, redirect, url_for
from .borrow_context import BorrowContext
from .borrow_strategy import StandardBorrowStrategy
from .models import User, Equipment

borrow_bp = Blueprint('borrow', __name__)

@borrow_bp.route('/catalog')
def catalog():
    items = Equipment.query.all()
    return render_template('catalog.html', items=items)

@borrow_bp.route('/borrow/<int:item_id>', methods=['GET', 'POST'])
def borrow_form(item_id):
    item = Equipment.query.get(item_id)
    if request.method == 'POST':
        user = User.query.get(1)
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
