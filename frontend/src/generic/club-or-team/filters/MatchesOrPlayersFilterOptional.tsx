import { Club } from "../../../types/Club";
import { SPLIT_BY_TYPE } from "../../../types/enums";
import { Season } from "../../../types/Season";
import { Team } from "../../../types/Team";
import { OppositionFilter } from "../matches/OppositionFilter";
import { SeasonFilter } from "../matches/SeasonFilter";
import { TeamFilter } from "../matches/TeamFilter";
import { MinAppsFilter } from "../players/MinAppsFilter";

interface OwnProps {
    club?:Club
    team?:Team
    clubSeasons:Record<string,Season[]>
    selectedTeamId:string
    setSelectedTeamId:Function
    setTeamSeasons:Function
    selectedSeason:string
    setSelectedSeason:Function
    teamSeasons:Season[]
    selectedSplitBy:string
    selectedOpposition:string
    setSelectedOpposition:Function
    oppositionOptions:string[]
    perGame?:boolean
    minApps:number
    setMinApps:Function
}

export const MatchesOrPlayersFilterOptional = (props:OwnProps) => {
    
    const getSeasons = () => {
        if (props.team) {
            return props.teamSeasons;
        }
        if (props.clubSeasons && (props.selectedTeamId != "")) {
            return props.clubSeasons[props.selectedTeamId]
        }
        return []
    }
    
    return (
        <div> 
            <h4 className="small-caps-subtitle">
                OPTIONAL FILTERS
            </h4>           
            {
                props.club && (
                    <TeamFilter
                        club={props.club}
                        selectedTeamId={props.selectedTeamId}
                        setSelectedTeamId={props.setSelectedTeamId}
                        clubSeasons={props.clubSeasons!}
                        setTeamSeasons={props.setTeamSeasons}
                    />
                )
            }
            <SeasonFilter
                selectedSeason={props.selectedSeason}
                setSelectedSeason={props.setSelectedSeason}
                seasonOptions={getSeasons()}
            />
            {
                (props.selectedSplitBy == SPLIT_BY_TYPE.OPPOSITION) && (
                    <OppositionFilter
                        selectedOpposition={props.selectedOpposition}
                        setSelectedOpposition={props.setSelectedOpposition}
                        oppositionOptions={props.oppositionOptions}
                    />
                )
            }
            {
                (props.perGame) && (
                    <MinAppsFilter
                        minApps={props.minApps}
                        setMinApps={props.setMinApps}
                    />
                )
            }
        </div>
    );
}