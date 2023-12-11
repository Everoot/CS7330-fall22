import numpy as np

import blueprints.new_data as nd
from blueprints.link_entryquery import link_team_basic_query


def link_standing(season_id, team_id, point):
    from app import db
    result = db['standing'].find_one({'season_id': season_id, 'team_id': team_id})
    if result is None:
        nd.new_standing(season_id, team_id, point)
    else:
        standing_id = result['_id']
        new_point = result['point'] + point
        db['standing'].update_one({"_id": standing_id}, {"$set": {"point": new_point}})


def link_score_input(game_id, score1, score2):
    from app import db
    result = db['game'].find_one({'_id': game_id})
    if result is None:
        # Game not exists
        return "Game not exists"
    else:
        # Game exists
        season_id = result['season_id']
        team1_id = result['team_id'][0]
        team2_id = result['team_id'][1]
        result = db['score'].find_one({'game_id': game_id})
        if result is not None:
            return "Game has scores"
        else:
            nd.new_score(game_id, score1, score2)
            # Set the points
            if score1 > score2:
                point1 = 3
                point2 = 0
            elif score1 < score2:
                point1 = 0
                point2 = 3
            else:
                point1 = 1
                point2 = 1

            # Update the standing
            link_standing(season_id, team1_id, point1)
            link_standing(season_id, team2_id, point2)
            return "Score added"


def link_team_season_records_query(team_name, season_id):
    from app import db
    result = link_team_basic_query(team_name)
    team_name = result['team_name']
    field = result['field']
    city = result['city']
    state = result['state']
    rating = result['rating']
    result = db['team'].find_one({'name': team_name})
    team_id = result['_id']
    result = db['game'].find({'season_id': season_id, 'team_id': team_id})
    team_game = []
    if result is not None:
        for x in result:
            game_id = x['_id']
            score_result = db['score'].find_one({'game_id': game_id})
            if score_result is not None:
                team_result = x['team_id']
                team1_name = db['team'].find_one({'_id': team_result[0]})['name']
                team2_name = db['team'].find_one({'_id': team_result[1]})['name']
                game_date = x['date']
                score1 = score_result['score1']
                score2 = score_result['score2']
                add_point = "+0"
                if score1 > score2:
                    add_point = "+3"
                elif score1 == score2:
                    add_point = "+1"
                find_game = {'team1_name': team1_name, 'team2_name': team2_name,
                             'score1': score1, 'score2': score2, 'add_point': add_point, 'game_date': game_date}
                team_game.append(find_game)
    team = {'team_name': team_name, 'field': field, 'city': city, 'state': state, 'rating': rating,
            'team_game': team_game}
    return team


def link_find_game(x, team1, team2):
    season_id = x['season_id']
    from app import db
    season_result = db['season'].find_one({'_id': season_id})
    season_name = season_result['name']
    league_id = season_result['league_id']
    league_name = db['league'].find_one({'_id': league_id})['name']
    field_id = x['location_id']
    field_result = db['field'].find_one({'_id': field_id})
    game_field = field_result['name']
    city_id = field_result['city_id']
    field_result = db['city'].find_one({'_id': city_id})
    game_city = field_result['name']
    game_state = field_result['state']
    game_date = x['date']
    score_result = db['score'].find_one({'game_id': x['_id']})
    score1 = score_result['score1']
    score2 = score_result['score2']
    add_point = "+0"
    if score1 > score2:
        add_point = "+3"
    elif score1 == score2:
        add_point = "+1"
    find_game = {'league_name': league_name, 'season_name': season_name,
                 'game_field': game_field, 'game_city': game_city, 'game_state': game_state,
                 'team1': team1, 'team2': team2,
                 'score1': score1, 'score2': score2, 'add_point': add_point, 'game_date': game_date}
    return find_game


# Substitute characteristic value for rating
def calculate_rating(league_id):
    from app import db
    result = db['team'].find({'league_id': league_id})
    team_id = []
    for x in result:
        team_id.append(x['_id'])
    n = len(team_id)
    i = 0
    j = 0
    m = [[0]*n for i in range(n)]
    for i in range(0, n):
        t1 = team_id[i]
        for j in range(0, n):
            t2 = team_id[j]
            t1t2 = db['game'].find({'team_id': [t1, t2]})
            for k in t1t2:
                score = db['score'].find_one({'game_id': k['_id']})
                if score is not None:
                    score1 = score['score1']
                    score2 = score['score2']
                    if score1 > score2:
                        m[i][j] += 1
                    elif score1 < score2:
                        m[i][j] -= 1
            t2t1 = db['game'].find({'team_id': [t2, t1]})
    c = np.linalg.eig(m)[0]
    i = 0
    for i in range(0, n):
        db['team'].update_one({"_id": team_id}, {"$set": {'rating': str(c[i])}})
    return 0