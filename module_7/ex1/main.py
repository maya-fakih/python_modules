from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, power: int, toughness: int):
        super().__init__(name, cost, rarity)
        self.power = power
        self.toughness = toughness
    
    def play(self, game_state: dict) -> dict:
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
            'effect': 'Creature summoned to battlefield'
        }

def main():
    print("\n=== DataDeck Deck Builder ===\n")
    
    print("Building deck with different card types...")
    
    deck = Deck()
    
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 5, "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Epic", 5, 4)
    
    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)
    
    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}\n")
    
    print("Drawing and playing cards:")
    
    deck.shuffle()
    
    game_state = {
        'player_mana': 10,
        'hand': [],
        'battlefield': [],
        'played_this_turn': []
    }
    
    for i in range(3):
        card = deck.draw_card()
        if card:
            print(f"Drew: {card.name} ({type(card).__name__})")
            
            game_state['hand'].append(card)
            
            result = card.play(game_state)
            print(f"Play result: {result}")
    
    print("\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()