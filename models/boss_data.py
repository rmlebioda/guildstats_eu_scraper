from distutils.util import change_root
from itertools import chain
import re

from attr import dataclass


@dataclass
class BossChances:
    """Class representing boss spawn chances per world"""
    world: str
    chances: str
    last_seen: str
    last_update: str

    def get_chances(self) -> float:
        """Returns numeric value of odds for boss to spawn

        Returns:
            float: chances for boss to spawn
        """
        chances = re.findall(r"\d+\.\d+", self.chances)
        return float(chances[0]) if len(chances) == 1 else float(0)

    def get_chances_text_value(self) -> int:
        """Returns numeric value of chances, the higher number, the higher ods of it's spawning, can be useful for sorting

        Returns:
            int: numeric value represeting importance of chances for the boss to spawn
        """
        if self.chances.lower().startswith('high chance'):
            return 2
        elif self.chances.lower().startswith('low'):
            return 1
        elif self.chances.lower().startswith('No chance'):
            return 0
        return -1

    def __str__(self):
        return f'world: {self.world} \tchances: {self.chances}\t{self.last_seen}\t({self.last_update})'

    def last_seen_days(self) -> int:
        """Returns number of days last seen of boss (or 0 in case of error)

        Returns:
            int: last seen days value
        """
        days = re.findall(r"(\d+) days", self.last_seen)
        if len(days) > 0:
            return int(days[0])
        return 0

@dataclass
class BossData:
    """Class representing data about boss"""

    name: str
    data: BossChances
    
    def __str__(self):
        return f'{self.name}:\t{self.data}'
