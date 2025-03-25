from typing import List
from game.animal import AnimalDeck, AnimalCard
from game.player import Player, HumanPlayer, ComputerPlayer
from datetime import datetime


class AuctionGame:
    def __init__(self, players: List[Player] = []):
        self.players = players
        self.animal_deck = AnimalDeck()
        self.current_round = 0
        self.human_player_index = 0
        self.current_player_index = 0
        self.created_at = datetime.now()
        self.mode = "auction"

    def run_bidding(self, owner: Player, current_card: AnimalCard):
        # Determine the owner of the current animal card
        current_bid = 0

        for bidder in self.players:
            if bidder.is_human:
                pass # TODO: Implement human bidding
            elif not bidder == owner:
                new_bid = bidder.bid(owner, current_bid, self.current_card, self.players)
                print(f"{bidder.name} bids {new_bid}")
                current_bid = max(current_bid, new_bid)
        
        print(f"{owner.name} wins the auction with a bid of {current_bid}")

    def run_horse_trading(self):
        pass

    def run_round(self):
        current_player = self.players[self.current_player_index]
        # let the current player decide to bid or trade
        self.mode = current_player.decide()
        if self.mode == "auction":
            self.current_card = self.animal_deck.draw()
            # display the current card in html
            self.run_bidding(current_player, self.current_card)
        elif self.mode == "horse_trading":
            self.run_horse_trading()


