import { useParams } from "react-router-dom"
import { LinkBarInfo } from "../../../types/LinkBarInfo";
import { LinkBar } from "../../../generic/LinkBar";

interface OwnProps {
    isClubAdmin:boolean
    clubId:string
}

export const TeamLinkBar = (props:OwnProps) => {

    let { teamId } = useParams();
    
    const getLinks = () => {
        var links = [
            {
                label: 'Club Overview',
                to: `/club/${props.clubId}/overview`
            },
            {
                label: 'Team Overview',
                to: `/team/${teamId}/overview`
            },
            {
                label: 'Update Data',
                to: `/team/${teamId}/update-data`,
                adminRequired: true
            },
            {
                label: 'Matches',
                to: `/team/${teamId}/matches`
            },
            {
                label: 'Player Leaderboards',
                to: `/team/${teamId}/players`
            }
        ] as LinkBarInfo[];
        return links;
    }
    
    return (
        <LinkBar
            links={getLinks()}
            isClubAdmin={props.isClubAdmin}
        />
    )
}