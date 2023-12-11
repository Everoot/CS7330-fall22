def link_delete_team(team_name):
    from app import db
    result = db['team'].find_one({'name': team_name})
    if result is None:
        return "Team not exists"
    else:
        team_id = result['_id']
        result = db['game'].find({'team_id': team_id})
        if result is not None:
            return "Team has games"
        else:
            db['team'].delete_one({'_id': team_id})
            return "Team deleted"


def link_delete_league(league_name):  #🌹
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        return "League not exists"
    else:
        league_id = result['_id']
        result = db['season'].find({'league_id': league_id})
        if result is not None:
            return "League has seasons"
        else:
            result = db['team'].find({'league_id': league_id})
            if result is not None:
                return "League has teams"
            else:
                db['league'].delete_one({'_id': league_id})
                return "League deleted"
