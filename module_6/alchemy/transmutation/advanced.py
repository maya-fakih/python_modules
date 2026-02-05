from ..potions import healing_potion
from .basic import lead_to_gold


def philosophers_stone():
    lead = lead_to_gold()
    heal = healing_potion()
    create = "Philosopher's stone created using"
    return f"{create} {lead} and {heal}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
