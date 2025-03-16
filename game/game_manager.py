import datetime
import uuid
from typing import Dict, Any, List
import random

from game.player import HumanPlayer, ComputerPlayer
from game.game import AuctionGame


class GameManager:
    def __init__(self):
        self.games: Dict[str, Dict[str, Any]] = {}
        self.names = ["Emma", "Liam", "Sophia", "Noah", "Olivia", "Jackson", "Ava", "Ethan", "Isabella", "Mason", "Charlotte", "James", "Amelia", "Benjamin", "Mia", "Alexander", "Harper", "William", "Evelyn", "Michael"]
        random.shuffle(self.names)

    def create_new_game(self) -> str:
        """Create a new game session and return its ID."""
        game_id = str(uuid.uuid4())
        self.games[game_id] = AuctionGame(players=[HumanPlayer("You")])
        return game_id

    def get_game(self, game_id: str) -> AuctionGame:
        """Get the current state of a game."""
        if game_id not in self.games:
            raise ValueError("Game not found")
        return self.games[game_id]

    def add_player(self, game_id: str) -> bool:
        """Add a computer player to the game."""
        if game_id not in self.games:
            return False
        
        game = self.games[game_id]
        player_name = self.names[len(game.players) - 1]
        # Check if player name is already taken
        if any(p.name == player_name for p in game.players):
            return False
            
        game.players.append(ComputerPlayer(player_name))
        print(game.players)
        return True

    def get_players(self, game_id: str) -> List[Any]:
        """Get the list of players in the game."""
        if game_id not in self.games:
            raise ValueError("Game not found")
        return self.games[game_id].players
