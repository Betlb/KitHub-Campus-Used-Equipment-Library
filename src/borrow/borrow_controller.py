from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .borrow_context import BorrowContext
from ..db.models import Equipment
from ..db.db import db
from .borrow_strategy import get_strategy_for_user

from .equipment_search.base import BaseEquipmentSearch
from .equipment_search.search_filter import SearchFilterDecorator
from .equipment_search.availability_filter import AvailabilityFilterDecorator
from .equipment_search.category_filter import CategoryFilterDecorator

borrow_bp = Blueprint('borrow', __name__)

@borrow_bp.route('/catalog')
def catalog():
    search_strategy = BaseEquipmentSearch()

    search_term = request.args.get('search', '').strip()
    if search_term:
        search_strategy = SearchFilterDecorator(search_strategy, search_term)


    category = request.args.get('category', '').strip()
    if category:
        search_strategy = CategoryFilterDecorator(search_strategy, category)


    search_strategy = AvailabilityFilterDecorator(search_strategy)

    items = search_strategy.search().all()
    return render_template('catalog.html', items=items)


@borrow_bp.route('/borrow/<int:item_id>', methods=['GET', 'POST'])
@login_required
def borrow_form(item_id):
    item = Equipment.query.get_or_404(item_id)
    user = current_user
    strategy = get_strategy_for_user(user)
    max_duration = strategy.get_max_duration()
    if request.method == 'POST':
        context = BorrowContext(strategy)
        try:
            # BorrowContext creates the request
            context.borrow(user, item, notes=request.form.get("notes", ""))
            return redirect(url_for('borrow.confirmation'))
        except Exception as e:
            return render_template('borrow_form.html', item=item, max_duration=max_duration, error=str(e))
    return render_template('borrow_form.html', item=item, max_duration=max_duration)

@borrow_bp.route('/confirmation')
@login_required
def confirmation():
    return render_template('confirmation.html')
