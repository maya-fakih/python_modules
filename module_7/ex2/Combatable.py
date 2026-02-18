from abc import ABC, abstractmethod
from typing import Dict, Any

class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        pass
    
    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass
    
    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass