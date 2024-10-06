import re
from typing import Optional
from ..models import Team, Player


def extractPlayerFromUrl(team: Team, url: str) -> Optional[Player]:
    match = re.match(
        r'^.*?/player/_/id/(.+?)/(.+)$',
        url,
        flags=re.IGNORECASE
    )
    
    if match:
        return Player(
            key=match.group(1),
            short_name=match.group(2),
            team=team.key
        )
    
    return None
