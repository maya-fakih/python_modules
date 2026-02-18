from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turn_count = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, f: CardFactory, s: GameStrategy) -> None:
        self.factory = f
        self.strategy = s

    def simulate_turn(self) -> dict:
        if not self.factory:
            return {'error': 'Engine not configured'}

        if not self.strategy:
            return {'error': 'Engine not configured'}

        self.turn_count = self.turn_count + 1

        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)

        cards_to_remove = []

        for card_name in turn_result['cards_played']:
            for i in range(len(self.hand)):
                card = self.hand[i]
                if card.name == card_name:
                    cards_to_remove.append(i)
                    if hasattr(card, 'durability'):
                        self.battlefield.append(card)
                    elif hasattr(card, 'health'):
                        self.battlefield.append(card)
                    break

        cards_to_remove.sort()
        cards_to_remove.reverse()

        for i in cards_to_remove:
            self.hand.pop(i)

        self.total_damage = self.total_damage + turn_result['damage_dealt']

        return turn_result

    def get_engine_status(self) -> dict:
        strategy_name = 'None'

        if self.strategy:
            strategy_name = self.strategy.get_strategy_name()

        return {
            'turns_simulated': self.turn_count,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
