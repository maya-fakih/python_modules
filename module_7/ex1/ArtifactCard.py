from typing import Dict
from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.is_active = True
    
    def play(self, game_state: dict) -> Dict:
        """Play the artifact card - places it into play permanently"""
        if 'hand' in game_state and self in game_state['hand']:
            game_state['hand'].remove(self)
        
        if 'battlefield' not in game_state:
            game_state['battlefield'] = []
        game_state['battlefield'].append(self)
        
        if 'played_this_turn' not in game_state:
            game_state['played_this_turn'] = []
        game_state['played_this_turn'].append(self.name)
        
        if 'player_mana' in game_state:
            game_state['player_mana'] -= self.cost
        
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}'
        }
    
    def activate_ability(self) -> Dict:
        """Activate the artifact's ability"""
        if self.durability <= 0:
            return {'error': 'Artifact has no durability left'}
        
        self.durability -= 1
        if self.durability <= 0:
            self.is_active = False
        
        return {
            'artifact_name': self.name,
            'ability_activated': self.effect,
            'durability_remaining': max(0, self.durability),
            'is_active': self.is_active
        }