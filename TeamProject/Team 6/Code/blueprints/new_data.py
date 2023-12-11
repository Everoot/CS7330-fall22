def new_league(name):
    league = {
        'name': name
    }
    from app import db
    db['league'].insert_one(league)
    new_id = db['league'].find_one({'name': name})['_id']
    return new_id


def new_commissioner(league_id, name, ssn):
    commissioner = {
        'league_id': league_id,
        'name': name,
        'ssn': ssn
    }
    from app import db
    db['commissioner'].insert_one(commissioner)
    new_id = db['commissioner'].find_one({'name': name})['_id']
    return new_id


def new_city(name, state):
    city = {
        'name': name,
        'state': state
    }
    from app import db
    db['city'].insert_one(city)
    new_id = db['city'].find_one({'name': name, 'state': state})['_id']
    return new_id


def new_field(city_id, name):
    field = {
        'city_id': city_id,
        'name': name
    }
    from app import db
    db['field'].insert_one(field)
    new_id = db['field'].find_one({'city_id': city_id, 'name': name})['_id']
    return new_id


def new_team(league_id, court_id, name, rating):
    team = {
        'league_id': league_id,
        'field_id': court_id,
        'name': name,
        'rating': rating
    }
    from app import db
    db['team'].insert_one(team)
    new_id = db['team'].find_one({'name': name})['_id']
    return new_id


def new_season(league_id, name, field_id, begin_date, end_date):
    season = {
        'league_id': league_id,
        'name': name,
        'field_id': field_id,
        'begin_date': begin_date,
        'end_date': end_date
    }
    from app import db
    db['season'].insert_one(season)
    new_id = db['season'].find_one({'name': name})['_id']
    return new_id


def new_game(season_id, location_id, date, team1_id, team2_id):
    game = {
        'season_id': season_id,
        'location_id': location_id,
        'date': date,
        'team_id': [team1_id, team2_id]
    }
    from app import db
    db['game'].insert_one(game)
    new_id = db['game'].find_one({'season_id': season_id, 'date': date})['_id']
    return new_id


def new_score(game_id, score1, score2):
    score = {
        'game_id': game_id,
        'score1': score1,
        'score2': score2
    }
    from app import db
    db['score'].insert_one(score)
    new_id = db['score'].find_one({'game_id': game_id})['_id']
    return new_id


def new_standing(season_id, team_id, point):
    standing = {
        'season_id': season_id,
        'team_id': team_id,
        'point': point
    }
    from app import db
    db['standing'].insert_one(standing)
    new_id = db['standing'].find_one({'season_id': season_id, 'team_id': team_id})['_id']
    return new_id


def new_user(name, password):
    user = {
        'name': name,
        'password': password
    }
    from app import db
    db['user'].insert_one(user)


def new_time(time):
    # 存一下时间
    time = {
        'time': time
    }
    from app import db
    db['time'].insert_one(time)
