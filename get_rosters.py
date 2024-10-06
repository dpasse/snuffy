import os
import sys

import time
from typing import Dict, List

sys.path.insert(0, './src')

from package.requests import Browser
from package.models import Team, Player
from package.parsers.players import extractPlayerFromUrl


def create_config_entry(sport: str) -> dict:
    return {
        'output': f'./output/{sport}/rosters.json',
        'source': f'./output/{sport}/teams.json'
    }

sports = ['nfl', 'mlb', 'nba', 'wnba', 'nhl']
mappings = { sport: create_config_entry(sport) for sport in sports }

def run(sport: str) -> None:
    config = mappings[sport]

    teams: List[Team] = []
    with open(config['source'], 'r') as teams_file:
        teams = Team.schema().loads(teams_file.read(), many=True)

    players: Dict[str, Player] = {}

    with Browser() as browser:
        for team in teams:
            bs = browser.make_request(url=team.get_roster())

            for link in bs.select('.Roster__MixedTables .Table__TD .AnchorLink'):
                player = extractPlayerFromUrl(team, link['href'])

                if player:
                    players[player.key] = player
            
            time.sleep(60)

    all_players = list(players.values())
    with open(os.path.join(config['output']), 'w') as output_file:
        output_file.write(
            Player.schema().dumps(all_players, many=True, indent=4)
        )


if __name__ == '__main__':
    sport = sys.argv[1]
    assert sport in sports

    run(sport)
