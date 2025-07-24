from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from functools import wraps
from .models import Equipment, User, BorrowRequest  # <-- Import BorrowRequest
from .db import db  # <-- Import db to make changes
from .inventory_manager import InventoryManager, LoggingObserver, NotificationObserver

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

inventory_manager = InventoryManager()
inventory_manager.attach(LoggingObserver())
inventory_manager.attach(NotificationObserver())

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# --- Admin Homepage Route  ---
@admin_bp.route('/home')
@login_required
@admin_required
def home():
    equipment_count = Equipment.query.count()
    user_count = User.query.count()
    available_items = Equipment.query.filter_by(status='available').count()
    return render_template('admin_home.html', equipment_count=equipment_count, user_count=user_count, available_items=available_items)

# --- Inventory Route  ---
@admin_bp.route('/inventory')
@login_required
@admin_required
def inventory_list():
    """Displays all equipment and finds any pending offers."""
    items = Equipment.query.order_by(Equipment.id).all()
    
    # Find all pending borrow requests
    pending_offers = BorrowRequest.query.filter_by(status='pending').all()
    
    # Create a dictionary for easy lookup in the template: {equipment_id: request_object}
    offers_map = {offer.equipment_id: offer for offer in pending_offers}
    
    return render_template('inventory.html', items=items, offers=offers_map)

# --- NEW: Routes for Handling Offers ---
@admin_bp.route('/offer/accept/<int:request_id>', methods=['POST'])
@login_required
@admin_required
def accept_offer(request_id):
    """Accepts a borrow request."""
    borrow_request = BorrowRequest.query.get_or_404(request_id)
    
    # Change request and equipment status
    borrow_request.status = 'approved'
    borrow_request.equipment.status = 'borrowed' # <-- Now the item is borrowed
    
    db.session.commit()
    flash(f'Offer for "{borrow_request.equipment.name}" has been accepted.', 'success')
    return redirect(url_for('admin.inventory_list'))


@admin_bp.route('/offer/reject/<int:request_id>', methods=['POST'])
@login_required
@admin_required
def reject_offer(request_id):
    """Rejects a borrow request."""
    borrow_request = BorrowRequest.query.get_or_404(request_id)
    
    borrow_request.status = 'rejected'
    
    db.session.commit()
    flash(f'Offer for "{borrow_request.equipment.name}" has been rejected.', 'danger')
    return redirect(url_for('admin.inventory_list'))

# --- Existing Inventory Management Routes ---
@admin_bp.route('/inventory/add', methods=['POST'])
@login_required
@admin_required
def add_equipment():
    name = request.form.get('name')
    category = request.form.get('category')
    inventory_manager.add_equipment(name, category)
    flash(f"Successfully added '{name}' to the inventory.", 'success')
    return redirect(url_for('admin.inventory_list'))

@admin_bp.route('/inventory/update-status/<int:item_id>', methods=['POST'])
@login_required
@admin_required
def update_status(item_id):
    new_status = request.form.get('status')
    inventory_manager.update_equipment_status(item_id, new_status)
    flash('Equipment status updated successfully.', 'success')
    return redirect(url_for('admin.inventory_list'))