import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0
        self.platform_status = 'active'

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards:
            return {'error': f'Card {card1_id} not found'}

        if card2_id not in self.cards:
            return {'error': f'Card {card2_id} not found'}

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played = self.matches_played + 1

        card1_power = card1.power
        card2_power = card2.power

        if card1_power > card2_power:
            winner_id = card1_id
            loser_id = card2_id
        elif card2_power > card1_power:
            winner_id = card2_id
            loser_id = card1_id
        else:
            if random.randint(1, 2) == 1:
                winner_id = card1_id
                loser_id = card2_id
            else:
                winner_id = card2_id
                loser_id = card1_id

        winner = self.cards[winner_id]
        loser = self.cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)

        winner.calculate_rating()
        loser.calculate_rating()

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())
        sorted_cards = sorted(
            cards_list,
            key=lambda x: x.rating,
            reverse=True
        )

        leaderboard = []

        for i in range(len(sorted_cards)):
            card = sorted_cards[i]
            leaderboard.append({
                'rank': i + 1,
                'name': card.name,
                'card_id': card.card_id,
                'rating': card.rating,
                'wins': card.wins,
                'losses': card.losses
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        if total_cards == 0:
            return {
                'total_cards': 0,
                'matches_played': self.matches_played,
                'avg_rating': 0,
                'platform_status': self.platform_status
            }

        total_rating = 0

        for card_id in self.cards:
            card = self.cards[card_id]
            total_rating = total_rating + card.rating

        avg_rating = total_rating // total_cards

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': self.platform_status
        }
