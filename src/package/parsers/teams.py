import re
from typing import Optional
from ..models import Team, SportType


def convertToSportType(sport: str) -> SportType:
    if sport == 'nfl':
        return SportType.NFL
    
    if sport == 'mlb':
        return SportType.MLB
    
    if sport == 'nba':
        return SportType.NBA
    
    if sport == 'wnba':
        return SportType.WNBA
    
    if sport == 'nhl':
        return SportType.NHL
    
    raise NotImplemented(f'"{sport}" has not been setup.')


def extractTeamFromUrl(url: str) -> Optional[Team]:
    match = re.match(
        r'^/(\w+)/team/_/name/(\w+)/(.+)$',
        url,
        flags=re.IGNORECASE
    )

    if match:
        return Team(
            key=match.group(3),
            short_name=match.group(2),
            sport=convertToSportType(match.group(1))
        )
    
    return None
