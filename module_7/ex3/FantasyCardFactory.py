import random
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_names = (
            [
                'Fire Dragon', 'Goblin Warrior', 'Elf Archer', 'Orc Brute',
                'Stone Golem'
            ]
        )
        self.spell_names = (
            [
                'Fireball', 'Lightning Bolt', 'Frost Nova', 'Healing Light',
                'Poison Dart'
            ]
        )
        self.artifact_names = (
            [
                'Mana Ring', 'Staff of Power', 'Crystal Ball',
                'Amulet of Protection', 'Goblin Bomb'
            ]
        )
        self.rarities = ['Common', 'Rare', 'Epic', 'Legendary']

    def create_creature(self, name_or_power=None):
        if isinstance(name_or_power, int):
            power = name_or_power
            name = random.choice(self.creature_names)
        elif isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(3, 7)
        else:
            name = random.choice(self.creature_names)
            power = random.randint(3, 7)

        cost = max(1, power - 2)
        health = power + random.randint(1, 3)
        rarity = random.choice(self.rarities)

        return CreatureCard(name, cost, rarity, power, health)

    def create_spell(self, name_or_power=None):
        if isinstance(name_or_power, int):
            power = name_or_power
            name = random.choice(self.spell_names)
        elif isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(2, 5)
        else:
            name = random.choice(self.spell_names)
            power = random.randint(2, 5)
        cost = power
        if 'Fire' in name or 'Lightning' in name:
            effect_type = 'damage'
        else:
            effect_type = random.choice(['damage', 'heal', 'buff', 'debuff'])
        rarity = random.choice(self.rarities)
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power=None):
        if isinstance(name_or_power, int):
            power = name_or_power
            name = random.choice(self.artifact_names)
        elif isinstance(name_or_power, str):
            name = name_or_power
            power = random.randint(2, 4)
        else:
            name = random.choice(self.artifact_names)
            power = random.randint(2, 4)
        cost = power
        durability = random.randint(3, 6)
        options = [
                    '+1 mana per turn', 'Draw extra card',
                    'Reduce spell cost', '+2 power to creatures'
                ]
        effect = random.choice(options)
        rarity = random.choice(self.rarities)

        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                deck.append(self.create_creature())
            elif card_type == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {
            'deck': deck,
            'size': len(deck),
            'factory': 'FantasyCardFactory',
            'theme': 'Fantasy'
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin', 'elf', 'orc', 'golem'],
            'spells': ['fireball', 'lightning', 'frost', 'heal', 'poison'],
            'artifacts': ['mana_ring', 'staff', 'crystal', 'amulet', 'bomb']
        }
