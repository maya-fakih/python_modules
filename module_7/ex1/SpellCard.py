from typing import Dict
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> Dict:
        """Play the spell card - consumes it from hand"""
        if 'hand' in game_state and self in game_state['hand']:
            game_state['hand'].remove(self)

        if 'played_this_turn' not in game_state:
            game_state['played_this_turn'] = []
        game_state['played_this_turn'].append(self.name)

        if 'player_mana' in game_state:
            game_state['player_mana'] -= self.cost

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f"{self.effect_type} spell effect"
        }

    def resolve_effect(self, targets: list) -> Dict:
        """Resolve the spell's effect on targets"""
        effect_descriptions = {
            'damage': f'Dealt damage to {len(targets)} target(s)',
            'heal': f'Healed {len(targets)} target(s)',
            'buff': f'Buffed {len(targets)} target(s)',
            'debuff': f'Debuffed {len(targets)} target(s)'
        }

        result = effect_descriptions.get(self.effect_type, 'Effect resolved')
        return {
            'spell_name': self.name,
            'effect_type': self.effect_type,
            'targets': len(targets),
            'result': result
        }
