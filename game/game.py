from typing import List
from game.animal import AnimalDeck
from game.player import Player
from datetime import datetime


class AuctionGame:
    def __init__(self, players: List[Player] = []):
        self.players = players
        self.animal_deck = AnimalDeck()
        self.current_card = self.animal_deck.draw()
        self.current_round = 0
        self.human_player_index = 0
        self.current_player_index = 0
        self.created_at = datetime.now()

    def run_bidding(self):
        owner = self.players[self.current_player_index]
        bidders = [player for player in self.players if player != owner]

        for bidder in bidders:
            print(f"{bidder.name} is bidding against {owner.name}")
            bid = input("Enter your bid: ")
            owner.bid(bid)


