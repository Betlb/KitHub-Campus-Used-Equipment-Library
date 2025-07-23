from .base import EquipmentSearch
from ..models import Equipment

class AvailabilityFilterDecorator(EquipmentSearch):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def search(self):
        return self.wrapped.search().filter(Equipment.status == 'available')
