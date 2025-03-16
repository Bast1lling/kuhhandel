from typing import List
from abc import ABC, abstractmethod
from game.money import MoneyCard
from game.llm import generate_structured_response
from game.prompts.schemas import BidResponse

class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.money: List[MoneyCard] = self._init_money()
        self.is_human = False  # Default to False in base class
        
    def _init_money(self) -> List[MoneyCard]:
        return [MoneyCard(0) for _ in range(3)] + [MoneyCard(10) for _ in range(4)] + [MoneyCard(50)]
    
    @abstractmethod
    def bid(self, current_bid: int):
        pass


class HumanPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = True
    
    def bid(self, current_bid: int):
        pass

class ComputerPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = False

    def bid(self, current_bid: int):
        pass


def test_bid():
    print(generate_structured_response("gpt-4o-mini", "How much should I bid for this keyboard?", BidResponse))

