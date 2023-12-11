from flask import render_template, request, Blueprint, url_for
from jsonpath import jsonpath
import jsonpath
from blueprints.link_entryquery import link_league_basic_query, link_league_champions_query, link_team_basic_query,link_team_records_query,link_game_query,link_rating_query,link_season_query
entry_query = Blueprint("query", __name__, url_prefix="/query")  # 创建一个蓝图


def str_None(a):
    if a is None or len(a) == 0 or a.isspace() is True:
        return True
    else:
        return False

def str_transfer(a):
    a = ''.join(a.split())
    a = str.lower(a)
    return a

def date_back(a):
    year = a[0:4]
    month = a[4:6]
    day = a[6:8]
    list = [year, month, day]
    a = '-'.join(list)
    return a

# def link_league_detail_query(league_name):
#     if league_name == 'league1':
#         result = {
#             "league_name": "league1",  # 联盟名字
#             "commissioner": "Jo",  # commissioner name
#             "seasons": {
#                 "20220601": {  # season_name
#                     "champion1": {  # team_name
#                         "rating": "10",
#                         "game_record": {
#                             "record1": "team2",         # 对打team_name
#                             "game_date": "20110101",
#                             "game_location": "Dallas",
#                             "game_score": "10",
#                         },
#                     },
#                 },
#             }
#         }
#         json.dumps(result)
#         return result
#     else:
#         return 'no'


#result = link_league_detail_query('league1')
#print(result)
#print(type(result))
# print(json.dumps(result,indent=2))
#res = json.loads(str(result))
#print(result['league_name'])


#
# def link_team_basic_query(team_name):
#     if team_name == 'yes':
#         state = "TX"
#         city = "Dallas"
#         field = "alington"
#         rating = 10
#         list = []
#         list.append(state)
#         list.append(city)
#         list.append(field)
#         list.append(rating)
#         return list
#     else:
#         return "no"
#
# def link_team_detail_query(team_name):
#     if team_name == 'yes':
#         result = {
#             "team_name": "yes",
#             "state": "TX",
#             "city":"Dallas",
#             "field": "Alington",
#             "rating": "0",
#             "seasons":{
#                 "20210101":{      #season_name
#                     "numbers_games": "5",      # 打了多少场
#                     "numbers_win_games": "2",
#                     "numbers_lose_game": "3",
#                     "total_socres": "20",
#                     "team_against":{          # 对手
#                         "teamB_name": {
#                             "score_of_the_game": "2",
#                             "total_socres": "15",
#                         },
#                         "teamC_name":{
#                             "score_of_the_tame": "0",
#                             "total_scores": "-5",
#                         },
#
#                     }
#                 },
#             }
#         }
#         return result
#     else:
#         return "no"
#
#
# def link_game_query(team1, team2): # 判断它们是否存在于数据库，以及是否打过比赛
#     if team1=='yes1' and team2 == 'yes2':
#         result = {
#             "team1": "yes1",
#             "team2": "yes2",
#             "game_date": {
#                     "20121213":{
#                     "state": "TX",
#                     "city": "Dalls",
#                     "field": "smu",
#                     "Team1 score": "10",
#                     "Team2 score": "1",
#                     },
#                     "20231999":{
#                     "game_date": "20231999",
#                     "state": "OH",
#                     "city": "Cleverland",
#                     "field": "Akron",
#                     "Team1 score": "3",
#                     "Team2 score": "23",
#                 }
#             }
#         }
#         json.dumps(result)
#         return result
#     else:
#         return "no"
#
# def link_Season_query(league_name,season_name):
#     if league_name== "league1"  and season_name == "20220101" :
#         result = {
#                 "1": "yes",
#                 "2": "yes2",
#                 "3": "yes3",
#         }
#         return result
#     else:
#         return "no"
#
#
# def link_Rating_query(league_name, team_name):
#     if league_name == 'league1' and team_name == 'yes1':
#         result = {
#             "league_name": "league1",
#             "team_name": "yes1",
#             "result": {
#                 "list" :"list or json",
#             }
#         }
#         json.dumps(result)
#         return result
#     else:
#         return "no"

@entry_query.route('/query_basic_league', methods=['GET', 'POST'])
def league_basic_query():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(league_name)
                # ---------------------------------------------------------------
                db_result = link_league_basic_query(league_name)  # 🌹
                if db_result == 'League not exists':
                    # 不存在
                    result = str(db_result)
                    return render_template('query_basic_league.html', result=result, league_name='', commissioner_ssn='',
                                           commissioner='', season_name='')
                    # 是否存在
                else:
                    commissioner = db_result['commissioner_name']
                    commissioner_ssn = db_result['commissioner_ssn']
                    season_name = db_result['season']
                    #json.dumps(season_name)
                    return render_template('query_basic_league.html', league_name=league_name,
                                           commissioner=commissioner,
                                           season=season_name, commissioner_ssn = commissioner_ssn)

                # league_name, commissioner, ssn
    return render_template('query_basic_league.html')


# Query 1 B  ✅
@entry_query.route('/query_detial_league', methods=['GET', 'POST'])
def league_champions_query():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(league_name)
                # -----------------------------------------------
                db_result = link_league_champions_query(league_name)  # 🌹
                print(type(db_result))
                #print(db_result)
                if db_result == 'League not exists':
                    # 不存在
                    result = str(db_result)
                    return render_template('query_detail_league.html', result=result, league_name='',
                                           commissioner='', season_name='', seasons = '')
                else:
                    # return render_template('query_detail_league.html', result=db_result, league_name='',
                    #                        commissioner='', season_name='', seasons = '')
                    # # 是否存在
                # else:
                    db_basic = link_league_basic_query(league_name)
                    commissioner = db_basic["commissioner_name"]
                    seasons = db_result.get('season_champion')
                    print(seasons)
                    return render_template('query_detail_league.html', league_name=league_name,
                                           commissioner = commissioner,
                                           seasons = seasons)
    return render_template('query_detail_league.html')


# Query 2 A ✅
@entry_query.route('/query_basic_team', methods=['GET', 'POST'])
def team_basic_query():
    if request.method == 'POST':
        team_name = request.form.get('teamname')
        if str_None(team_name):
            return 'The team name cannot be null.'
        else:
            team_name = str_transfer(team_name)
            if not str.isalnum(team_name):
                return 'Please enter right 26 characters which can combine the numbers in team name'
            else:
                print(team_name)
                # -----------------------------------------                                        🌹
                db_result = link_team_basic_query(team_name)
                if db_result == 'Team not exists':
                    # 不存在
                    error = str(db_result)
                    return render_template('query_basic_team.html', error=error, team_name='', city='', field='',
                                           rating='')
                    # 是否存在
                else:
                    state = db_result['state']
                    city = db_result['city']
                    field = db_result['field']
                    rating = db_result['rating']
                    return render_template('query_basic_team.html', team_name = team_name, state = state, city=city, field=field,
                                           rating=rating)
    return render_template('query_basic_team.html')

# Query 2 B ✅
@entry_query.route('/query_detail_team', methods=['GET', 'POST'])
def team_records_query():
    if request.method == 'POST':
        team_name = request.form.get('teamname')
        if str_None(team_name):
            return 'The team name cannot be null.'
        else:
            team_name = str_transfer(team_name)
            if not str.isalnum(team_name):
                return 'Please enter right 26 characters which can combine the numbers in team name'
            else:
                print(team_name)
                db_result = link_team_records_query(team_name)                  # --------------------- 🌹
                print(db_result)
                print(type(db_result))
                if db_result == 'Team not exists':
                    # 不存在
                    error = str(db_result)
                    return render_template('query_detail_team.html', error=error, team_name='', city='', field='',
                                           rating='', state='')
                    # 是否存在
                else:
                    state = db_result.get('state')
                    city = db_result.get('city')
                    field = db_result.get('field')
                    rating = db_result.get('rating')
                    # team_game = db_result.get(list(db_result.keys())[-1])
                    team_game = db_result.get('team_game')
                    return render_template('query_detail_team.html', team_name=team_name, city=city, field=field,
                                           rating=rating, state=state, team_game = team_game)
    return render_template('query_detail_team.html')


# Query 3 ✅
@entry_query.route('/query_game', methods=['GET', 'POST'])
def game_query():
    if request.method == 'POST':
        team_name_a = request.form.get('teamnamea')
        if str_None(team_name_a):
            return 'The team A name cannot be null.'
        else:
            team_name_a = str_transfer(team_name_a)
            if not str.isalnum(team_name_a):
                return 'Please enter right 26 characters which can combine the numbers in team A name'
            else:
                print(team_name_a)
                team_name_b = request.form.get('teamnameb')
                if str_None(team_name_b):
                    return 'The team B name cannot be null.'
                else:
                    team_name_b = str_transfer(team_name_b)
                    if not str.isalnum(team_name_b):
                        return 'Please enter right 26 characters which can combine the numbers in team B name'
                    else:
                        print(team_name_b)
                        db_result = link_game_query(team_name_a,team_name_b)  # --------------------- 🌹
                        #if db_result == 'Both teams not exists' or "Team 1 not exists" or "Team 2 not exists"
                            # 不存在
                            #error = str(db_result)
                        #    return render_template('query_game.html', error=error, result = '', team1 ='', team2='')
                            # 是否存在
                        if type(db_result) == str:
                            error = str(db_result)
                        else:
                            error = ''
                        return render_template('query_game.html', error = error, team1 = team_name_a,
                                                   team2 = team_name_b,
                                                   result = db_result)
    return render_template('query_game.html')

# 4. season query ✅
@entry_query.route('/query_season', methods=['GET', 'POST'])
def season_query():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(league_name)
                season_name = request.form.get('seasonname')
                if str_None(season_name):
                    return 'The season name cannot be null.'
                else:
                    season_name = str_transfer(season_name)
                    if not str.isalnum(season_name):
                        return 'Please enter right 26 characters which can combine the numbers in season name.'
                    else:
                        print(season_name)
                        db_result = link_season_query(league_name, season_name)  # --------------------- 🌹
                        if type(db_result) == str:
                            error = str(db_result)
                            return render_template('query_season.html', error=error, league_name = '', season_name ='')
                            # 是否存在
                        else:
                            return render_template('query_season.html', error = '', league_name = league_name,
                                                   season_name = season_name, result = db_result['season_standing'])

    return render_template('query_season.html')

# 5. Rating query
@entry_query.route('/query_rating', methods=['GET', 'POST'])
def rating_query():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(league_name)
                db_result = link_rating_query(league_name)  # --------------------- 🌹
                print(type(db_result))
                if type(db_result) == str:  # ✅
                            # 不存在
                    error = str(db_result)
                    return render_template('query_rating.html', error=error, league_name='')
                            # 是否存在
                else:
                    return render_template('query_rating.html', error='', league_name=league_name,result = db_result)
    return render_template('query_rating.html')
 #