import re

from attr import dataclass


@dataclass
class BossChances:
    """Class representing boss spawn chances per world"""
    world: str
    chances: str
    last_seen: str
    last_update: str

    def extract_chances(self) -> float:
        chances = re.findall(r"\d+\.\d+", self.chances)
        return float(chances[0]) if len(chances) == 1 else float(0)

    def __str__(self):
        return f'world: {self.world} \tchances: {self.chances}\t{self.last_seen}\t({self.last_update})'

@dataclass
class BossData:
    """Class representing data about boss"""

    name: str
    data: BossChances
    
    def __str__(self):
        return f'{self.name}:\t{self.data}'
