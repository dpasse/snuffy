from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


class SportType(Enum):
    NFL = 'nfl'
    MLB = 'mlb'
    NBA = 'nba'
    WNBA = 'wnba'
    NHL = 'nhl'


@dataclass_json
@dataclass
class Team:
    key: str
    short_name: str
    sport: SportType

    def get_url(self) -> str:
        return f'https://www.espn.com/{self.sport.value}/team/_/name/{self.key}/{self.short_name}'

    def get_roster(self) -> str:
        return f'https://www.espn.com/{self.sport.value}/team/roster/_/name/{self.short_name}/{self.key}'
