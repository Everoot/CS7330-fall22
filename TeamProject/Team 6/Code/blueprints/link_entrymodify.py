from blueprints.new_data import new_time


def link_update_input(update):
    from app import db
    result = db['time'].find_one()
    if result is not None:
        db['time'].delete_one({})
    new_time(update)
    return "Time updated"


def link_move_team(move_team_name, league_name_future):
    from app import db
    # check team
    result = db['team'].find_one({'name': move_team_name})
    if result is None:
        return "Move_team not exists"
    else:
        # check time
        team_id = result['_id']
        old_id = result['league_id']
        time = db['time'].find_one()['time']
        result = db['season'].find_one({'league_id': old_id,
                                        'begin_date': {"$lte": time}, 'end_date': {"$gte": time}})
        if result is not None:
            return "Time for old league not available"
        else:
            result = db['league'].find_one({'name': league_name_future})
            if result is None:
                # league_name unqualified
                return "League_future not exists"
            elif result['_id'] == old_id:
                return "Same league"
            else:
                new_id = result['_id']

                result = db['season'].find_one({'league_id': new_id,
                                                'begin_date': {"$lte": time}, 'end_date': {"$gte": time}})
                if result is not None:
                    return "Time for new league not available"
                else:
                    db['team'].update_one({"_id": team_id}, {"$set": {'league_id': new_id}})
                    return "Move successfully"
