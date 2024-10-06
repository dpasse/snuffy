from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Player:
    key: str
    short_name: str
    team: str

    def get_player(self) -> str:
        return f'https://www.espn.com/nfl/player/_/id/{self.key}/{self.short_name}'
