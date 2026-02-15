from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health:
                 int) -> None:
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be +ve")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        })
        return info

    def play(self, game_state: Dict) -> Dict:
        return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefeild",
            }

    def attack_target(self, target: str) -> Dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True,
        }
