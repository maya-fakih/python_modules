from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=(
            lambda x: getattr(x, 'health', 100) if hasattr(x, 'health') else
            100)
        )

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        total_mana_used = 0
        damage_dealt = 0
        mana = 10

        for card in sorted(hand, key=lambda x: x.cost):
            if card.cost <= mana:
                mana -= card.cost
                total_mana_used += card.cost
                cards_played.append(card.name)

                if hasattr(card, 'power'):
                    damage_dealt += card.power
                elif (hasattr(card, 'effect_type') and
                        card.effect_type == 'damage'):
                    damage_dealt += card.cost

        targets_attacked = []
        if battlefield:
            targets = self.prioritize_targets(battlefield)
            for target in targets[:2]:
                if hasattr(target, 'name'):
                    targets_attacked.append(target.name)
                else:
                    targets_attacked.append(str(target))

        if not targets_attacked:
            targets_attacked = ['Enemy Player']
            damage_dealt += 3

        return {
            'cards_played': cards_played,
            'mana_used': total_mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt,
            'mana_remaining': mana
        }
