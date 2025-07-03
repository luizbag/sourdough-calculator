from dataclasses import dataclass
from enum import Enum


class IngredientKind(Enum):
    Flour = 1
    Water = 2
    Other = 3


@dataclass
class Ingredient():
    name: str
    percentage: float
    kind: IngredientKind
