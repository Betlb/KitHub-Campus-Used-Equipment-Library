from abc import ABC, abstractmethod
from ...db.models import Equipment

class EquipmentSearch(ABC):
    @abstractmethod
    def search(self):
        pass

class BaseEquipmentSearch(EquipmentSearch):
    def search(self):
        return Equipment.query
