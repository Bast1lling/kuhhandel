import datetime
import uuid
from typing import Dict, Any, List

from game.player import HumanPlayer, ComputerPlayer

class GameManager:
    def __init__(self):
        self.games: Dict[str, Dict[str, Any]] = {}

    def create_new_game(self) -> str:
        """Create a new game session and return its ID."""
        game_id = str(uuid.uuid4())
        self.games[game_id] = {
            'state': 'initializing',
            'players': [HumanPlayer("You")],
            'current_round': 0,
            'created_at': datetime.datetime.now()
        }
        return game_id

    def get_game_state(self, game_id: str) -> Dict[str, Any]:
        """Get the current state of a game."""
        if game_id not in self.games:
            raise ValueError("Game not found")
        return self.games[game_id]

    def add_player(self, game_id: str, player_name: str) -> bool:
        """Add a computer player to the game."""
        if game_id not in self.games:
            return False
        
        game = self.games[game_id]
        if game['state'] != 'initializing':
            return False
            
        # Check if player name is already taken
        if any(p.name == player_name for p in game['players']):
            return False
            
        game['players'].append(ComputerPlayer(player_name))
        return True

    def get_players(self, game_id: str) -> List[Any]:
        """Get the list of players in the game."""
        if game_id not in self.games:
            raise ValueError("Game not found")
        return self.games[game_id]['players'] 