from typing import Dict, List, Optional
import random
from ex0.Card import Card

class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.discard_pile: List[Card] = []
    
    def add_card(self, card: Card) -> None:
        """Add a card to the deck"""
        self.cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name"""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                removed_card = self.cards.pop(i)
                return True
        return False
    
    def shuffle(self) -> None:
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw_card(self) -> Optional[Card]:
        """Draw a card from the deck"""
        if not self.cards:
            if self.discard_pile:
                self.cards = self.discard_pile.copy()
                self.discard_pile = []
                self.shuffle()
            else:
                return None
        
        if self.cards:
            drawn_card = self.cards.pop(0)
            return drawn_card
        return None
    
    def get_deck_stats(self) -> Dict:
        """Get statistics about the deck"""
        total_cards = len(self.cards) + len(self.discard_pile)
        
        creature_count = 0
        spell_count = 0
        artifact_count = 0
        total_cost = 0
        
        all_cards = self.cards + self.discard_pile
        for card in all_cards:
            total_cost += card.cost
            
            card_type = type(card).__name__
            if 'Creature' in card_type:
                creature_count += 1
            elif 'Spell' in card_type:
                spell_count += 1
            elif 'Artifact' in card_type:
                artifact_count += 1
        
        avg_cost = total_cost / total_cards if total_cards > 0 else 0
        
        return {
            'total_cards': total_cards,
            'creatures': creature_count,
            'spells': spell_count,
            'artifacts': artifact_count,
            'avg_cost': round(avg_cost, 1)
        }