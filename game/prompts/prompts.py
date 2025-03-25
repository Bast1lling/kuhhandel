"""
This module contains prompt templates and instructions for LLM interactions.
"""

from langchain.prompts import PromptTemplate
import os
from typing import List

dir_path = os.path.dirname(os.path.abspath(__file__))

def get_rule_description() -> str:
    with open(os.path.join(dir_path, "instructions", "game_rules.txt"), "r") as file:
        return PromptTemplate(template=file.read(), input_variables=[]).format()
    

def get_game_state_description(player, others: List) -> str:
    description = "Here is the current state of the game:\n"
    for other_player in others:
        if other_player == player:
            continue
        description += f"{other_player.name} has {len(other_player.money)} money cards and these animal cards:\n"
        for animal, count in other_player.animals.items():
            if count > 0:
                description += f"{animal.name} x {count}\n"
    
    description += f"You have these money cards:\n"
    for money, count in player.money.items():
        if count > 0:
            description += f"Money Card {money} x {count}\n"   
    description += f"You have these animal cards:\n"
    for animal, count in player.animals.items():
        if count > 0:
            description += f"{animal.name} x {count}\n"
    return description


def get_bid_instruction(name: str, bid: int, animal: str) -> str:
    with open(os.path.join(dir_path, "instructions", "bid_instruction.txt"), "r") as file:
        template = PromptTemplate(template=file.read(), input_variables=["name", "bid", "animal"])
    
    return template.format(name=name, bid=bid, animal=animal)
