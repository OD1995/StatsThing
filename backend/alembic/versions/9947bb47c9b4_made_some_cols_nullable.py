"""made some cols nullable

Revision ID: 9947bb47c9b4
Revises: de9d4426c8e9
Create Date: 2024-11-30 15:24:47.454964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '9947bb47c9b4'
down_revision: Union[str, None] = 'de9d4426c8e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_users_user_id', 'club_admins', type_='foreignkey')
    op.drop_constraint('fk_clubs_club_id', 'club_admins', type_='foreignkey')
    op.create_foreign_key('fk_clubs_club_id', 'club_admins', 'clubs', ['club_id'], ['club_id'])
    op.create_foreign_key('fk_users_user_id', 'club_admins', 'users', ['user_id'], ['user_id'])
    op.alter_column('competitions', 'data_source_competition_id',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_constraint('fk_team_seasons_team_season_id', 'competitions', type_='foreignkey')
    op.create_foreign_key('fk_team_seasons_team_season_id', 'competitions', 'team_seasons', ['team_season_id'], ['team_season_id'])
    op.drop_constraint('fk_leagues_league_id', 'league_seasons', type_='foreignkey')
    op.create_foreign_key('fk_leagues_league_id', 'league_seasons', 'leagues', ['league_id'], ['league_id'])
    op.drop_constraint('fk_data_sources_data_source_id', 'leagues', type_='foreignkey')
    op.create_foreign_key('fk_data_sources_data_source_id', 'leagues', 'data_sources', ['data_source_id'], ['data_source_id'])
    op.drop_constraint('fk_matches_match_id', 'match_errors', type_='foreignkey')
    op.create_foreign_key('fk_matches_match_id', 'match_errors', 'matches', ['match_id'], ['match_id'])
    op.drop_constraint('team_seasons_team_season_id', 'matches', type_='foreignkey')
    op.drop_constraint('fk_competitions_competition_id', 'matches', type_='foreignkey')
    op.create_foreign_key('fk_competitions_competition_id', 'matches', 'competitions', ['competition_id'], ['competition_id'])
    op.create_foreign_key('team_seasons_team_season_id', 'matches', 'team_seasons', ['team_season_id'], ['team_season_id'])
    op.drop_constraint('fk_data_sources_data_source_id', 'metrics', type_='foreignkey')
    op.create_foreign_key('fk_data_sources_data_source_id', 'metrics', 'data_sources', ['data_source_id'], ['data_source_id'])
    op.drop_constraint('fk_matches_match_id', 'player_match_performances', type_='foreignkey')
    op.drop_constraint('fk_metrics_metric_id', 'player_match_performances', type_='foreignkey')
    op.drop_constraint('fk_players_player_id', 'player_match_performances', type_='foreignkey')
    op.create_foreign_key('fk_matches_match_id', 'player_match_performances', 'matches', ['match_id'], ['match_id'])
    op.create_foreign_key('fk_metrics_metric_id', 'player_match_performances', 'metrics', ['metric_id'], ['metric_id'])
    op.create_foreign_key('fk_players_player_id', 'player_match_performances', 'players', ['player_id'], ['player_id'])
    op.alter_column('players', 'better_player_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_constraint('fk_clubs_club_id', 'players', type_='foreignkey')
    op.create_foreign_key('fk_clubs_club_id', 'players', 'clubs', ['club_id'], ['club_id'])
    op.drop_constraint('fk_teams_team_id', 'team_leagues', type_='foreignkey')
    op.drop_constraint('fk_leagues_league_id', 'team_leagues', type_='foreignkey')
    op.create_foreign_key('fk_teams_team_id', 'team_leagues', 'teams', ['team_id'], ['team_id'])
    op.create_foreign_key('fk_leagues_league_id', 'team_leagues', 'leagues', ['league_id'], ['league_id'])
    op.drop_constraint('fk_teams_team_id', 'team_names', type_='foreignkey')
    op.create_foreign_key('fk_teams_team_id', 'team_names', 'teams', ['team_id'], ['team_id'])
    op.drop_constraint('fk_teams_team_id', 'team_seasons', type_='foreignkey')
    op.drop_constraint('fk_league_seasons_league_season_id', 'team_seasons', type_='foreignkey')
    op.create_foreign_key('fk_teams_team_id', 'team_seasons', 'teams', ['team_id'], ['team_id'])
    op.create_foreign_key('fk_league_seasons_league_season_id', 'team_seasons', 'league_seasons', ['league_season_id'], ['league_season_id'])
    op.drop_constraint('fk_sports_sport_id', 'teams', type_='foreignkey')
    op.drop_constraint('fk_clubs_club_id', 'teams', type_='foreignkey')
    op.drop_constraint('fk_data_sources_data_source_id', 'teams', type_='foreignkey')
    op.create_foreign_key('fk_sports_sport_id', 'teams', 'sports', ['sport_id'], ['sport_id'])
    op.create_foreign_key('fk_data_sources_data_source_id', 'teams', 'data_sources', ['data_source_id'], ['data_source_id'])
    op.create_foreign_key('fk_clubs_club_id', 'teams', 'clubs', ['club_id'], ['club_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_clubs_club_id', 'teams', type_='foreignkey')
    op.drop_constraint('fk_data_sources_data_source_id', 'teams', type_='foreignkey')
    op.drop_constraint('fk_sports_sport_id', 'teams', type_='foreignkey')
    op.create_foreign_key('fk_data_sources_data_source_id', 'teams', 'data_sources', ['data_source_id'], ['data_source_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_clubs_club_id', 'teams', 'clubs', ['club_id'], ['club_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_sports_sport_id', 'teams', 'sports', ['sport_id'], ['sport_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_league_seasons_league_season_id', 'team_seasons', type_='foreignkey')
    op.drop_constraint('fk_teams_team_id', 'team_seasons', type_='foreignkey')
    op.create_foreign_key('fk_league_seasons_league_season_id', 'team_seasons', 'league_seasons', ['league_season_id'], ['league_season_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_teams_team_id', 'team_seasons', 'teams', ['team_id'], ['team_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_teams_team_id', 'team_names', type_='foreignkey')
    op.create_foreign_key('fk_teams_team_id', 'team_names', 'teams', ['team_id'], ['team_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_leagues_league_id', 'team_leagues', type_='foreignkey')
    op.drop_constraint('fk_teams_team_id', 'team_leagues', type_='foreignkey')
    op.create_foreign_key('fk_leagues_league_id', 'team_leagues', 'leagues', ['league_id'], ['league_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_teams_team_id', 'team_leagues', 'teams', ['team_id'], ['team_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_clubs_club_id', 'players', type_='foreignkey')
    op.create_foreign_key('fk_clubs_club_id', 'players', 'clubs', ['club_id'], ['club_id'], referent_schema='squad_stats')
    op.alter_column('players', 'better_player_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_constraint('fk_players_player_id', 'player_match_performances', type_='foreignkey')
    op.drop_constraint('fk_metrics_metric_id', 'player_match_performances', type_='foreignkey')
    op.drop_constraint('fk_matches_match_id', 'player_match_performances', type_='foreignkey')
    op.create_foreign_key('fk_players_player_id', 'player_match_performances', 'players', ['player_id'], ['player_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_metrics_metric_id', 'player_match_performances', 'metrics', ['metric_id'], ['metric_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_matches_match_id', 'player_match_performances', 'matches', ['match_id'], ['match_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_data_sources_data_source_id', 'metrics', type_='foreignkey')
    op.create_foreign_key('fk_data_sources_data_source_id', 'metrics', 'data_sources', ['data_source_id'], ['data_source_id'], referent_schema='squad_stats')
    op.drop_constraint('team_seasons_team_season_id', 'matches', type_='foreignkey')
    op.drop_constraint('fk_competitions_competition_id', 'matches', type_='foreignkey')
    op.create_foreign_key('fk_competitions_competition_id', 'matches', 'competitions', ['competition_id'], ['competition_id'], referent_schema='squad_stats')
    op.create_foreign_key('team_seasons_team_season_id', 'matches', 'team_seasons', ['team_season_id'], ['team_season_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_matches_match_id', 'match_errors', type_='foreignkey')
    op.create_foreign_key('fk_matches_match_id', 'match_errors', 'matches', ['match_id'], ['match_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_data_sources_data_source_id', 'leagues', type_='foreignkey')
    op.create_foreign_key('fk_data_sources_data_source_id', 'leagues', 'data_sources', ['data_source_id'], ['data_source_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_leagues_league_id', 'league_seasons', type_='foreignkey')
    op.create_foreign_key('fk_leagues_league_id', 'league_seasons', 'leagues', ['league_id'], ['league_id'], referent_schema='squad_stats')
    op.drop_constraint('fk_team_seasons_team_season_id', 'competitions', type_='foreignkey')
    op.create_foreign_key('fk_team_seasons_team_season_id', 'competitions', 'team_seasons', ['team_season_id'], ['team_season_id'], referent_schema='squad_stats')
    op.alter_column('competitions', 'data_source_competition_id',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_constraint('fk_users_user_id', 'club_admins', type_='foreignkey')
    op.drop_constraint('fk_clubs_club_id', 'club_admins', type_='foreignkey')
    op.create_foreign_key('fk_clubs_club_id', 'club_admins', 'clubs', ['club_id'], ['club_id'], referent_schema='squad_stats')
    op.create_foreign_key('fk_users_user_id', 'club_admins', 'users', ['user_id'], ['user_id'], referent_schema='squad_stats')
    # ### end Alembic commands ###
