import os
import sys

from typing import List

sys.path.insert(0, './src')

from package.requests import make_request
from package.models import Team
from package.parsers.teams import extractTeamFromUrl


def create_config_entry(sport: str) -> dict:
    return {
        'output': f'./output/{sport}/',
        'source': f'https://www.espn.com/{sport}/standings/_/group/league'
    }

sports = ['nfl', 'mlb', 'nba', 'wnba', 'nhl']
mappings = { sport: create_config_entry(sport) for sport in sports }

def run(sport: str) -> None:
    if not sport in mappings:
        raise NotImplemented()
    
    teams: List[Team] = []
    config = mappings[sport]

    bs = make_request(url=config['source'])
    for link in bs.select('.team-link .AnchorLink'):
        team = extractTeamFromUrl(link['href'])
        if team:
            teams.append(team)

        team.to_json()

    with open(os.path.join(config['output'], 'teams.json'), 'w') as output_file:
        output_file.write(
            Team.schema().dumps(teams, many=True, indent=4)
        )

if __name__ == '__main__':
    sport = sys.argv[1]
    assert sport in sports
    
    run(sport)
