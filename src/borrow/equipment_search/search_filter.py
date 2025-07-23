from sqlalchemy import or_
from .base import EquipmentSearch
from src.borrow.models import Equipment

class SearchFilterDecorator(EquipmentSearch):
    def __init__(self, wrapped, search_term):
        self.wrapped = wrapped
        self.search_term = search_term

    def search(self):
        return self.wrapped.search().filter(
            or_(
                Equipment.name.ilike(f"%{self.search_term}%"),
                Equipment.category.ilike(f"%{self.search_term}%")
            )
        )
