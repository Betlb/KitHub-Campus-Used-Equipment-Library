from .observer import Subject, Observer
from .db import db
from .models import Equipment

# --- Concrete Subject ---
class InventoryManager(Subject):
    """
    Manages inventory operations and notifies observers of changes.
    This is our concrete Subject.
    """
    def add_equipment(self, name, category):
        """Adds a new piece of equipment to the database and notifies observers."""
        new_equipment = Equipment(name=name, category=category, status='available')
        db.session.add(new_equipment)
        db.session.commit()
        print(f"INVENTORY_MANAGER: Added '{name}' to inventory.")
        
        self.notify(event="EQUIPMENT_ADDED", data=new_equipment)
        return new_equipment

    def update_equipment_status(self, equipment_id, new_status: str):
        """Updates the status of an existing piece of equipment and notifies observers."""
        equipment = Equipment.query.get(equipment_id)
        if not equipment:
            raise ValueError("Equipment not found.")
        
        equipment.status = new_status
        db.session.commit()
        print(f"INVENTORY_MANAGER: Updated status for '{equipment.name}' to '{new_status}'.")
        
        self.notify(event="STATUS_UPDATED", data=equipment)
        return equipment

# --- Concrete Observers ---
class LoggingObserver(Observer):
    """An observer that logs inventory changes to the console."""
    def update(self, subject, event, data=None):
        if event == "EQUIPMENT_ADDED":
            print(f"LOGGING_OBSERVER: New equipment added - ID: {data.id}, Name: {data.name}")
        elif event == "STATUS_UPDATED":
            print(f"LOGGING_OBSERVER: Equipment status changed - ID: {data.id}, New Status: {data.status}")

class NotificationObserver(Observer):
    """An observer that simulates sending a notification about inventory changes."""
    def update(self, subject, event, data=None):
        if event == "EQUIPMENT_ADDED" and data.category.lower() == "laptop":
            print(f"NOTIFICATION_OBSERVER: **High-priority alert!** New laptop '{data.name}' is now available.")
        elif event == "STATUS_UPDATED" and data.status == "maintenance":
            print(f"NOTIFICATION_OBSERVER: Item '{data.name}' has been sent for maintenance.")