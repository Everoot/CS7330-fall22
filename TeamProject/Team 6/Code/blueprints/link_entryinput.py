import blueprints.new_data as nd
import blueprints.link_others as lo
from blueprints.schedule import groupStage


def link_generate_random_table(league_name):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        league_id = result['_id']
        result = db['team'].find({'league_id': league_id})
        teams_name = []
        for x in result:
            teams_name.append(x['name'])
        result = groupStage(teams_name)
        return result


def link_league_input(league_name, commissioner, ssn):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is not None:
        # league_name unqualified
        return "League exist"
    else:
        # league_name qualified, check ssn
        result = db['commissioner'].find_one({'ssn': ssn})
        if result is not None:
            # ssn unqualified
            return "ssn exist"
        else:
            # create league
            league_id = nd.new_league(league_name)
            nd.new_commissioner(league_id, commissioner, ssn)
            return "League created"


def link_team_input(league_name, team_name, team_state, team_city, team_field, team_rating):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        # league_name qualified, check team_name
        league_id = result['_id']
        result = db['team'].find_one({'name': team_name})
        if result is not None:
            # team_name unqualified
            return "Team exist"
        else:
            # team_name qualified, check city
            result = db['city'].find_one({'name': team_city, 'state': team_state})
            if result is not None:
                # city exist, check field
                city_id = result['_id']
                result = db['field'].find_one({'city_id': result['_id'], 'name': team_field})
                if result is not None:
                    # field exist
                    field_id = result['_id']
                else:
                    field_id = nd.new_field(city_id, team_field)
            else:
                # city not exist
                city_id = nd.new_city(team_city, team_state)
                field_id = nd.new_field(city_id, team_field)
            # create team
            nd.new_team(league_id, field_id, team_name, team_rating)
            return "Team created"


def link_season_input(league_name, season_name, season_begin_date, season_end_date, season_state, season_city,
                      season_field):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        # league_name qualified, check season_name
        league_id = result['_id']
        result = db['season'].find_one({'league_id': league_id, 'name': season_name})
        if result is not None:
            # season_name unqualified
            return "Season exist"
        else:
            # season_name qualified, check date
            result1 = db['season'].find_one({'league_id': league_id,
                                             'begin_date': {"$gte": season_begin_date, "$lte": season_end_date}})
            result2 = db['season'].find_one({'league_id': league_id,
                                             'end_date': {"$gte": season_begin_date, "$lte": season_end_date}})
            result3 = db['season'].find_one({'league_id': league_id,
                                             'begin_date': {"$lte": season_begin_date},
                                             'end_date': {"$gte": season_end_date}})
            if result1 is not None or result2 is not None or result3 is not None:
                return "This league has season in the range"
            else:
                # date qualified, check city
                result = db['city'].find_one({'name': season_city, 'state': season_state})
                if result is not None:
                    # city exist, check field
                    city_id = result['_id']
                    result = db['field'].find_one({'city_id': result['_id'], 'name': season_field})
                    if result is not None:
                        # field exist
                        field_id = result['_id']
                    else:
                        field_id = nd.new_field(city_id, season_field)
                else:
                    # city not exist
                    city_id = nd.new_city(season_city, season_state)
                    field_id = nd.new_field(city_id, season_field)
                # create team
                nd.new_season(league_id, season_name, field_id, season_begin_date, season_end_date)
                return "Season created"


def link_game_input(league_name, season_name, team1, team2, game_date):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        # league_name qualified, check season_name
        league_id = result['_id']
        result = db['season'].find_one({'league_id': league_id, 'name': season_name})
        if result is None:
            # season_name unqualified
            return "Season not exist"
        elif result['begin_date'] > game_date or result['end_date'] < game_date:
            # season_name qualified, time unqualified
            return "Game date is not in the range"
        else:
            # season_name qualified, time qualified, check team
            season_id = result['_id']
            location_id = result["field_id"]
            result1 = db['team'].find_one({'name': team1})
            result2 = db['team'].find_one({'name': team2})

            if result1 is None and result2 is None:
                # both teams not exists
                return "Both teams not exists"
            else:
                # one team not exists
                if result1 is None:
                    return "Team 1 not exists"
                elif result2 is None:
                    return "Team 2 not exists"
                else:
                    # both team exists, check time
                    team1_id = result1['_id']
                    team2_id = result2['_id']
                    result1 = db["game"].find_one({'team_id': team1_id, 'date': game_date})
                    result2 = db["game"].find_one({'team_id': team2_id, 'date': game_date})
                    if result1 is not None and result2 is not None:
                        # both team have game in this date
                        return "Both teams have game in this date"
                    else:
                        # one team has game in this date
                        if result1 is not None:
                            return "Team 1 has game in this date"
                        elif result2 is not None:
                            return "Team 2 has game in this date"
                        else:
                            nd.new_game(season_id, location_id, game_date, team1_id, team2_id)
                            return "Game created"


def link_result_input(league_name, season_name, team1, team2, score1, score2, game_date):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        # league_name qualified, check season_name
        league_id = result['_id']
        result = db['season'].find_one({'league_id': league_id, 'name': season_name})
        if result is None:
            # season_name unqualified
            return "Season not exist"
        else:
            # season_name qualified, check team
            season_id = result['_id']
            result1 = db['team'].find_one({'name': team1})
            result2 = db['team'].find_one({'name': team2})

            if result1 is None and result2 is None:
                # both teams not exists
                return "Both teams not exists"
            else:
                # one team not exists
                if result1 is None:
                    return "Team 1 not exists"
                elif result2 is None:
                    return "Team 2 not exists"
                else:
                    # both team exists
                    team1_id = result1['_id']
                    team2_id = result2['_id']
                    result = db['game'].find_one({'season_id': season_id, 'date': game_date,
                                                  'team_id': [team1_id, team2_id]})
                    if result is None:
                        return "Game not exists"
                    else:
                        game_id = result['_id']
                        result = lo.link_score_input(game_id, score1, score2)
                        return result
