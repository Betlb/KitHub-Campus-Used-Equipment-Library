from ...db.models import Equipment
from .base import EquipmentSearch

class CategoryFilterDecorator(EquipmentSearch):
    def __init__(self, wrapped, category):
        self.wrapped = wrapped
        self.category = category.lower()

    def search(self):
        return self.wrapped.search().filter(Equipment.category.ilike(f"%{self.category}%"))
