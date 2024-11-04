from uuid import UUID
from sqlalchemy import ForeignKey, String
from app.models import Base
from sqlalchemy.orm import Mapped, mapped_column

class Competition(Base):
    __tablename__ = 'competitions'
    __table_args__ = {"mysql_engine": "InnoDB"}

    competition_id: Mapped[UUID] = mapped_column(primary_key=True)
    data_source_competition_id: Mapped[str] = mapped_column(String(100))
    competition_name: Mapped[str] = mapped_column(String(100))
    team_season_id: Mapped[UUID] = mapped_column(
        ForeignKey("team_seasons.team_season_id", name="fk_team_seasons_team_season_id"),
        index=True
    )