from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .borrow_context import BorrowContext
from .borrow_strategy import StandardBorrowStrategy
from .models import Equipment, User, BorrowRequest
from datetime import datetime, timedelta
from .db import db
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
    if request.method == 'POST':
        user = User.query.get(1) 
        strategy = get_strategy_for_user(user)
        context = BorrowContext(strategy)
        try:
            context.borrow(user, item)

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
