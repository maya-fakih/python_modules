from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 power: int, health: int, card_id: str):
        super().__init__(name, cost, rarity)
        self.power = power
        self.health = health
        self.max_health = health
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 1200
        self.is_alive = True

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
            'card_id': self.card_id,
            'mana_used': self.cost,
            'effect': 'Tournament card enters battlefield'
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
            'attacker_id': self.card_id,
            'target': target_name,
            'damage': damage,
            'target_status': target_status
        }

    def defend(self, incoming_damage: int) -> dict:
        if not self.is_alive:
            return {'error': f'{self.name} is already defeated'}

        damage_blocked = 0
        if incoming_damage > 3:
            damage_blocked = 1

        damage_taken = incoming_damage - damage_blocked

        self.health -= damage_taken
        if self.health <= 0:
            self.is_alive = False

        return {
            'defender': self.name,
            'defender_id': self.card_id,
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

    def calculate_rating(self) -> int:
        expected_score = 1 / (1 + 10 ** ((1200 - 1200) / 400))
        k_factor = 32
        actual_score = self.wins / (self.wins + self.losses + 0.1)
        rating_change = k_factor * (actual_score - expected_score)
        self.rating = self.rating + int(rating_change)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins = self.wins + wins

    def update_losses(self, losses: int) -> None:
        self.losses = self.losses + losses

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'card_id': self.card_id,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating,
            'record': f'{self.wins}-{self.losses}'
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'card_id': self.card_id,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating,
            'power': self.power,
            'health': self.health
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['card_id'] = self.card_id
        info['type'] = 'Tournament'
        info['power'] = self.power
        info['health'] = self.health
        info['wins'] = self.wins
        info['losses'] = self.losses
        info['rating'] = self.rating
        return info
