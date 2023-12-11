def link_league_basic_query(league_name):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        return "League not exists"
    else:
        league_id = result['_id']
        result = db['commissioner'].find_one({'league_id': league_id})
        commissioner_name = result['name']
        commissioner_ssn = result['ssn']
        result = db['season'].find({'league_id': league_id})
        season = []
        for x in result:
            season_name = x['name']
            field_id = x['field_id']
            result1 = db['field'].find_one({'_id': field_id})
            season_field = result1['name']
            city_id = result1['city_id']
            result1 = db['city'].find_one({'_id': city_id})
            season_city = result1['name']
            season_state = result1['state']
            season_begin_date = x['begin_date']
            season_end_date = x['end_date']
            find_season = {'season_name': season_name,
                           'season_field': season_field, 'season_city': season_city, 'season_state': season_state,
                           'season_begin_date': season_begin_date, 'season_end_date': season_end_date}
            season.append(find_season)
        league = {'league_name': league_name, 'commissioner_name': commissioner_name,
                  'commissioner_ssn': commissioner_ssn, 'season': season}
        return league


def link_league_champions_query(league_name):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        return "League not exists"
    else:
        result = link_league_basic_query(league_name)
        league_name = result['league_name']
        league_id = db['league'].find_one({'name': league_name})['_id']
        season = result['season']
        season_champion = []
        for x in season:
            season_name = x['season_name']
            season_id = db['season'].find_one({'league_id': league_id, 'name': season_name})['_id']
            standing = db['standing'].find({'season_id': season_id})
            if standing is not None:
                season_field = x['season_field']
                season_city = x['season_city']
                season_state = x['season_state']
                season_begin_date = x['season_begin_date']
                season_end_date = x['season_end_date']
                sorted_standing = sorted(standing, key=lambda i: i['point'], reverse=True)
                if sorted_standing is not None:
                    for x in range(0, len(sorted_standing)):
                        print(x, sorted_standing[x])
                    #champion_point = sorted_standing[0]['point']
                    champion_result = sorted_standing[0]
                    champion_point = champion_result['point']
                    champion = []
                    for y in sorted_standing:
                        if y['point'] == champion_point:
                            team_id = y['team_id']
                            team_name = db['team'].find_one({'_id': team_id})['name']
                            from blueprints.link_others import link_team_season_records_query
                            result = link_team_season_records_query(team_name, season_id)
                            champion.append(result)
                        else:
                            break
                    find_champion = {'season_name': season_name,
                                    'season_field': season_field, 'season_city': season_city, 'season_state': season_state,
                                    'season_begin_date': season_begin_date, 'season_end_date': season_end_date,
                                    'champion': champion}
                    season_champion.append(find_champion)

        league = {'league_name': league_name, 'season_champion': season_champion}
        return league


def link_team_basic_query(team_name):
    from app import db
    result = db['team'].find_one({'name': team_name})
    if result is None:
        return "Team not exists"
    else:
        result = db['team'].find_one({'name': team_name})
        rating = result['rating']
        field_id = result['field_id']
        result = db['field'].find_one({'_id': field_id})
        field = result['name']
        city_id = result['city_id']
        result = db['city'].find_one({'_id': city_id})
        city = result['name']
        state = result['state']
        team = {'team_name': team_name, 'field': field, 'city': city, 'state': state, 'rating': rating}
        return team


def link_team_records_query(team_name):
    from app import db
    result = db['team'].find_one({'name': team_name})
    if result is None:
        return "Team not exists"
    else:
        result = link_team_basic_query(team_name)
        team_name = result['team_name']
        field = result['field']
        city = result['city']
        state = result['state']
        rating = result['rating']
        result = db['team'].find_one({'name': team_name})
        team_id = result['_id']
        result = db['game'].find({'team_id': team_id})
        team_game = []

        for x in result:
            team_result = x['team_id']
            team1_name = db['team'].find_one({'_id': team_result[0]})['name']
            team2_name = db['team'].find_one({'_id': team_result[1]})['name']
            game_date = x['date']
            game_id = x['_id']
            season_id = x['season_id']
            season_result = db['season'].find_one({'_id': season_id})
            season_name = season_result['name']
            league_id = season_result['league_id']
            league_name = db['league'].find_one({'_id': league_id})['name']
            score_result = db['score'].find_one({'game_id': game_id})
            score1 = score_result['score1']
            score2 = score_result['score2']
            add_point = "+0"
            if score1 > score2:
                add_point = "+3"
            elif score1 == score2:
                add_point = "+1"
            find_game = {'league_name': league_name, 'season_name': season_name,
                         'team1_name': team1_name, 'team2_name': team2_name,
                         'score1': score1, 'score2': score2, 'add_point': add_point, 'game_date': game_date}
            team_game.append(find_game)
        team = {'team_name': team_name, 'field': field, 'city': city, 'state': state, 'rating': rating,
                'team_game': team_game}
        return team


def link_game_query(team1_name, team2_name):
    from app import db
    result1 = db['team'].find_one({'name': team1_name})
    result2 = db['team'].find_one({'name': team2_name})

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
            result = db['team'].find_one({'name': team1_name})
            team1_id = result['_id']
            result = db['team'].find_one({'name': team2_name})
            team2_id = result['_id']
            result1 = db['game'].find({'team_id': [team1_id, team2_id]})
            result2 = db['game'].find({'team_id': [team2_id, team1_id]})
            game = []
            from blueprints.link_others import link_find_game
            for x in result1:
                team1 = team1_name
                team2 = team2_name
                find_game = link_find_game(x, team1, team2)
                game.append(find_game)
            for y in result2:
                team2 = team1_name
                team1 = team2_name
                find_game = link_find_game(y, team1, team2)
                game.append(find_game)
            return game


def link_season_query(league_name, season_name):
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
            league_id = db['league'].find_one({'name': league_name})['_id']
            season_id = db['season'].find_one({'league_id': league_id, 'name': season_name})['_id']
            standing = db['standing'].find({'season_id': season_id})
            sorted_standing = sorted(standing, key=lambda i: i['point'], reverse=True)
            season_standing = []
            for x in sorted_standing:
                team_name = db['team'].find_one({'_id': x['team_id']})['name']
                point = x['point']
                find_standing = {'team_name': team_name, 'point': point}
                season_standing.append(find_standing)
            season = {'league_name': league_name, 'season_name': season_name, 'season_standing': season_standing}
            return season


def link_rating_query(league_name):
    from app import db
    result = db['league'].find_one({'name': league_name})
    if result is None:
        # league_name unqualified
        return "League not exist"
    else:
        league_id = result['_id']
        from blueprints.link_others import calculate_rating
        calculate_rating(league_id)
        result = db['team'].find({'league_id': league_id})
        sorted_result = sorted(result, key=lambda i: i['rating'], reverse=True)
        league_rating = []
        print(sorted_result)
        for x in sorted_result:
            print(x)
            team_id = x['_id']
            team_name = db['team'].find_one({'_id': team_id})['name']
            rating = {'team_name': team_name, 'rating': x['rating']}
            league_rating.append(rating)
    return league_rating

