from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, 
                 power: int, health: int, mana: int, spells: List[str]):
        super().__init__(name, cost, rarity)
        self.power = power
        self.health = health
        self.max_health = health
        self.is_alive = True
        self.mana = mana
        self.max_mana = mana
        self.spells = spells
        self.spell_effects = {
            'Fireball': 'Deals 4 damage',
            'Heal': 'Restores 3 health',
            'Lightning': 'Deals 5 damage',
            'Shield': 'Reduces incoming damage by 2'
        }
    
    def play(self, game_state: dict) -> dict:
        if 'hand' in game_state and self in game_state['hand']:
            game_state['hand'].remove(self)
        
        if 'battlefield' not in game_state:
            game_state['battlefield'] = []
        game_state['battlefield'].append(self)
        
        if 'player_mana' in game_state:
            game_state['player_mana'] -= self.cost
        
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'card_type': 'Elite',
            'effect': 'Elite card enters the battlefield'
        }
    
    def attack(self, target) -> dict:
        if not self.is_alive:
            return {'error': f'{self.name} is defeated'}
        
        damage = self.power
        
        if hasattr(target, 'health'):
            target.health -= damage
            if target.health <= 0:
                target.is_alive = False
                target_status = 'defeated'
            else:
                target_status = f'health reduced to {target.health}'
            target_name = target.name
        else:
            target_name = target
            target_status = 'damaged'
        
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': damage,
            'combat_type': 'melee',
            'target_status': target_status
        }
    
    def defend(self, incoming_damage: int) -> dict:
        if not self.is_alive:
            return {'error': f'{self.name} is already defeated'}
        
        damage_blocked = min(2, incoming_damage // 3)
        damage_taken = incoming_damage - damage_blocked
        
        self.health -= damage_taken
        if self.health <= 0:
            self.is_alive = False
        
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.is_alive
        }
    
    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'power': self.power,
            'health': self.health,
            'max_health': self.max_health,
            'is_alive': self.is_alive
        }
    
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if spell_name not in self.spells:
            return {'error': f'Unknown spell: {spell_name}'}
        
        if self.mana < 2:
            return {'error': 'Insufficient mana'}
        
        self.mana -= 2
        
        if spell_name == 'Heal' and targets and hasattr(targets[0], 'health'):
            targets[0].health = min(targets[0].max_health, targets[0].health + 3)
        
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [t.name if hasattr(t, 'name') else str(t) for t in targets],
            'mana_used': 2,
            'effect': self.spell_effects.get(spell_name, 'Casts a spell'),
            'mana_remaining': self.mana
        }
    
    def channel_mana(self, amount: int) -> dict:
        old_mana = self.mana
        self.mana = min(self.max_mana, self.mana + amount)
        actual_channeled = self.mana - old_mana
        
        return {
            'channeled': actual_channeled,
            'total_mana': self.mana,
            'max_mana': self.max_mana,
            'caster': self.name
        }
    
    def get_magic_stats(self) -> dict:
        return {
            'name': self.name,
            'mana': self.mana,
            'max_mana': self.max_mana,
            'spells': self.spells,
            'spell_count': len(self.spells)
        }
    
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': 'Elite',
            'power': self.power,
            'health': self.health,
            'mana': self.mana,
            'spells': self.spells
        })
        return info