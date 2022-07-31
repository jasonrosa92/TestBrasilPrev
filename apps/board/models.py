from django.db import models


from random import (
    randint,
    shuffle)
from dataclasses import dataclass
from typing import List, Tuple

from apps.user.models import (
    Player,
    IMPULSIVE,
    EXIGENT,
    CAUTIOUS,
    RANDOM)
from apps.property.models import Propertie


def roll_dice():
    return randint(1, 6)


@dataclass
class Gamer:
    player: int
    current_position: int = 0
    amount: float = 300.0
    shifts: int = 0


class Board(object):
    default_gamers = [
        Gamer(Player(behavior=IMPULSIVE)),
        Gamer(Player(behavior=EXIGENT)),
        Gamer(Player(behavior=CAUTIOUS)),
        Gamer(Player(behavior=RANDOM)),
    ]
    qty_properties: int
    properties = List[Propertie]
    gamers = List[Gamer]
    excludes = []
    players = List[Tuple]
    result = List[tuple]
    timeout = 0
    inner = None