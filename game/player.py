from typing import List
from abc import ABC, abstractmethod
from game.money import MoneyCard


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.money: List[MoneyCard] = self._init_money()
        self.is_human = False  # Default to False in base class
        
    def _init_money(self):
        self.money = [MoneyCard(0) for _ in range(3)] + [MoneyCard(10) for _ in range(4)] + [MoneyCard(50)]


class HumanPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = True

class ComputerPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_human = False
