from typing import List, Dict
from abc import ABC, abstractmethod
from game.llm import generate_structured_response
from game.prompts.schemas import BidResponse
from game.animal import AnimalCard, Animal
from game.prompts.prompts import get_game_state_description, get_bid_instruction, get_rule_description

class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.money: Dict[int, int] = {0: 3, 10: 4, 50: 1, 100: 0, 200: 0, 500: 0}  # Initial money distribution
        self.animals: Dict[Animal, int] = {x: 0 for x in Animal}
        self.is_human = False  # Default to False in base class
    
    @abstractmethod
    def bid(self, owner, current_bid: int, current_card: AnimalCard, others: List):
        pass

    @abstractmethod
    def decide(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name == other.name


class HumanPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = True
     
    def bid(self, owner: Player, current_bid: int, current_card: AnimalCard, others: List[Player]):
        pass

    def decide(self):
        return "bid"

class ComputerPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = False

    def bid(self, owner: Player, current_bid: int, current_card: AnimalCard, others: List[Player]):
        prompt = get_rule_description() + get_game_state_description(self, others) + get_bid_instruction(owner.name, current_bid, current_card.animal)
        response = generate_structured_response(prompt, BidResponse)
        return response["bid_amount"]
    
    def decide(self):
        return "bid"
