import os
import random
from enum import Enum


class Animal(Enum):
    ROOSTER = "Rooster"
    GOOSE = "Goose"
    CAT = "Cat"
    DOG = "Dog"
    SHEEP = "Sheep"
    GOAT = "Goat"
    DONKEY = "Donkey"
    PIG = "Pig"
    COW = "Cow"
    HORSE = "Horse"

    def cost(self):
        return {
            Animal.ROOSTER: 10,
            Animal.GOOSE: 40,
            Animal.CAT: 90,
            Animal.DOG: 160,
            Animal.SHEEP: 250,
            Animal.GOAT: 350,
            Animal.DONKEY: 500,
            Animal.PIG: 650,
            Animal.COW: 800,
            Animal.HORSE: 1000,
        }[self]
    
    def path_to_image(self):
        return f"assets/animals/{self.value.lower()}.jpg"

class AnimalCard:
    def __init__(self, type: Animal):
        self.type = type

class AnimalDeck:
    def __init__(self):
        self.cards = []
        for animal_type in Animal:
            for _ in range(4):
                self.cards.append(AnimalCard(animal_type))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def size(self):
        return len(self.cards)
