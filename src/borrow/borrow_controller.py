from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .borrow_context import BorrowContext
from .borrow_strategy import StandardBorrowStrategy
from .models import Equipment

borrow_bp = Blueprint('borrow', __name__)

@borrow_bp.route('/catalog')
def catalog():
    items = Equipment.query.all()
    return render_template('catalog.html', items=items)

@borrow_bp.route('/borrow/<int:item_id>', methods=['GET', 'POST'])
@login_required
def borrow_form(item_id):
    item = Equipment.query.get_or_404(item_id)
    if request.method == 'POST':
        strategy = StandardBorrowStrategy()
        context = BorrowContext(strategy)
        try:
            context.borrow(current_user, item)
            return redirect(url_for('borrow.confirmation'))
        except Exception as e:
            return render_template('borrow_form.html', item=item, error=str(e))
    return render_template('borrow_form.html', item=item)
