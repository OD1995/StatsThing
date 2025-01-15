from enum import Enum

class ClubType(Enum):
    COMPLETELY_NEW = 'completely-new'
    ALREADY_EXISTS = 'already-exists'

class DataSource(str, Enum):
    FOOTBALL_ASSOCIATION: str = 'football-association'
    MANUAL: str = 'manual'

class Sport(str, Enum):
    FOOTBALL: str = 'football'

class Result(str, Enum):
    WIN: str = 'W'
    DRAW: str = 'D'
    LOSS: str = 'L'

class HomeAwayNeutral(str, Enum):
    HOME: str = 'H'
    AWAY: str = 'A'
    NEUTRAL: str = 'N'

class Metric(str, Enum):
    APPEARANCES: str = 'Appearances'
    OVERALL_GOALS: str = 'Overall Goals'
    FEATURED_PLAYER: str = 'Featured Player'
    GOALS: str = 'Goals'
    ASSISTS: str = 'Assists'
    PLAYER_OF_MATCH: str = 'Player Of Match'

class SplitByType(str, Enum):
    NA: str = 'N/A'
    OPPOSITION: str = 'Opposition'
    PLAYER_COUNT: str = 'Player Count'
    SEASON: str = 'Season'
    YEAR: str = 'Year'

class LeaderboardType(str, Enum):    
    APPEARANCES: str = 'Appearances'
    APPEARANCES_BY_SEASON: str = 'Appearances By Season'
    APPEARANCES_BY_YEAR: str = 'Appearances By Year'
    GOALS: str = 'Goals'
    GOALS_PER_GAME: str = 'Goals Per Game'