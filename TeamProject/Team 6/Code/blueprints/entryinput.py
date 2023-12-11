import json

from flask import Flask, render_template, request, Blueprint, redirect, url_for
from datetime import datetime
from blueprints.link_entryinput import link_league_input, link_team_input, link_season_input, link_game_input, \
    link_result_input, link_generate_random_table

entry_input = Blueprint("enter", __name__, url_prefix="/add")  # 创建一个蓝图


def dictchangelist(a):
    dic1 = []

    dict(a)
    for index, i in enumerate(a):
        print(i)
        dic2 = {}
        for z, j in enumerate(i):
            print(z)
            print(j)
            z = str(z)
            c = {str(z): j}
            dic2.setdefault(z, j)
        dic1.append(dic2)

    return dic1


def str_None(a):
    if a is None or len(a) == 0 or a.isspace() is True:
        return True
    else:
        return False


def str_transfer(a):
    a = ''.join(a.split())
    a = str.lower(a)
    return a


def date_transfer(a):
    a = ''.join(a.split('-'))
    return a


def date_back(a):
    year = a[0:4]
    month = a[4:6]
    day = a[6:8]
    list = [year, month, day]
    a = '-'.join(list)
    return a


def listToJson(lst):
    import json
    import numpy as np
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    # str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return list_json


# def link_generate_random_table(league_name, season_name):
#     if league_name == "league1":
#         result =[{
#                     "team1": "yes1",
#                     "team2": "yes2",
#                     "date" : "20201201"
#                 },{
#                     "team1":"no1",
#                     "team2": "no2",
#                     "date": "20220202"
#                 }]
#         json.dumps(result)
#         return result
#     else:
#         return "no"

@entry_input.route('/add_new_game/generate_random_table', methods=['GET', 'POST'])
def generate_random_table():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                # print(league_nameb)
                # season_name = request.form.get('seasonname')
                # if str_None(season_name):
                #     return 'The season name cannot be null.'
                # else:
                #     # print(season_name)
                db_table = link_generate_random_table(league_name)

                print(type(db_table))
                # print(db_table)
                if db_table == "League not exist":
                    error = str(db_table)
                    return render_template('generate_random_table.html', error=error, result='')
                else:
                    # random_table_choose(db_table)
                    result = dictchangelist(db_table)
                    print(type(result))
                    # return render_template('generate_random_table.html', db_table= result)
                    return render_template('generate_random_table_choose.html', db_table=result)
                    # return redirect('/add/add_new_game/generate_random_table_choose',)
                # team_namea = request.form.get('teamnamea')
                # if str_None(team_namea):
                #     return 'The team A name cannot be null.'
                # else:
                #     team_namea = str_transfer(team_namea)
                #     if not str.isalnum(team_namea):
                #         return 'Please enter right 26 characters which can combine the numbers in team A name'
                #     else:
                #         # print(team_namea)
                #         team_nameb = request.form.get('teamnameb')
                #         if str_None(team_nameb):
                #             return 'The team B name cannot be null.'
                #         else:
                #             team_nameb = str_transfer(team_nameb)
                #             if not str.isalnum(team_namea):
                #                 return 'Please enter right 26 characters which can combine the numbers in team B name'
                #             else:
                #                 game_date = request.form.get('gamedate')
                #                 # print(game_date)
                #                 if str_None(game_date):
                #                     return 'The game date cannot be null.'
                #                 else:
                #                     game_date = date_transfer(game_date)
                #                     # print(game_date)
                #                     print(league_name, season_name, team_namea,
                #                           team_nameb, game_date)  # 🌹
    return render_template("generate_random_table.html")


@entry_input.route('/add_new_game/generate_random_table_choose', methods=['GET', 'POST'])
def generate_random_table_choose():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                # print(league_nameb)
                season_name = request.form.get('seasonname')
                if str_None(season_name):
                    return 'The season name cannot be null.'
                else:
                    # print(season_name)
                    team_namea = request.form.get('teamnamea')
                    if str_None(team_namea):
                        return 'The team A name cannot be null.'
                    else:
                        team_namea = str_transfer(team_namea)
                        if not str.isalnum(team_namea):
                            return 'Please enter right 26 characters which can combine the numbers in team A name'
                        else:
                            # print(team_namea)
                            team_nameb = request.form.get('teamnameb')
                            if str_None(team_nameb):
                                return 'The team B name cannot be null.'
                            else:
                                team_nameb = str_transfer(team_nameb)
                                if not str.isalnum(team_namea):
                                    return 'Please enter right 26 characters which can combine the numbers in team B name'
                                else:
                                    if team_namea == team_nameb:
                                        return 'Team can not play a game with themselves'
                                    game_date = request.form.get('gamedate')
                                    # print(game_date)
                                    if str_None(game_date):
                                        return 'The game date cannot be null.'
                                    else:
                                        game_date = date_transfer(game_date)
                                        # print(game_date)
                                        print(league_name, season_name, team_namea,
                                          team_nameb, game_date)  # 🌹
                                        db_result = link_game_input(league_name, season_name, team_namea, team_nameb,
                                                                game_date)
                                        db_table = link_generate_random_table(league_name)
                                        if db_table == "League not exist":
                                            db_table = str(db_table)
                                        else:
                                            # random_table_choose(db_table)
                                            db_table = dictchangelist(db_table)

                                        if db_result == "Game created":
                                            result = str(db_result)
                                            return render_template('generate_random_table_choose.html', error='', result=result,db_table=db_table)
                                        else:
                                            error = str(db_result)
                                            return render_template('generate_random_table_choose.html', error=error, result='',db_table=db_table)

    return render_template('generate_random_table_choose.html')


# ✅
@entry_input.route('/add_new_league', methods=['GET', 'POST'])  # 用该蓝图来设置路由
def league_input():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                commissioner = request.form.get('commissioner')
                if str_None(commissioner):
                    return 'The commissioner cannot be null.'
                else:
                    commissioner = str_transfer(commissioner)
                    if not str.isalnum(commissioner):
                        return 'Please enter right 26 characters which can combine the numbers in league name'
                    else:
                        # print(commissioner)
                        ssn = request.form.get('ssn')
                        if str_None(ssn):
                            return 'The ssn cannot be null.'
                        else:
                            ssn = str_transfer(ssn)
                            if not str.isdigit(ssn):
                                return 'Please enter right numbers.'
                            else:
                                # print(ssn)
                                print(league_name, commissioner, ssn)  # 🌹
                                db_result = link_league_input(league_name, commissioner, ssn)
                                if db_result == "League exist" or db_result == "ssn exist":
                                    error = str(db_result)
                                    return render_template('add_new_league.html', error=db_result, result='')
                                else:
                                    result = str(db_result)
                                    return render_template('add_new_league.html', error='', result=result)

    return render_template('add_new_league.html')


# ✅
@entry_input.route('/add_new_team', methods=['GET', 'POST'])
def team_input():
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
                team_state = request.form.get('teamstate')
                if str_None(team_state):
                    return 'The team state cannot be null.'
                else:
                    team_state = str_transfer(team_state)
                    if not str.isalnum(team_state):
                        return 'Please enter right 26 characters which can combine the numbers in team state.'
                    else:
                        print(team_state)
                        teamcity = request.form.get('teamcity')
                        if str_None(teamcity):
                            return 'The team city cannot be null.'
                        else:
                            teamcity = str_transfer(teamcity)
                            if not str.isalnum(teamcity):
                                return 'Please enter right 26 characters which can combine the numbers in teamcity'
                            else:
                                print(teamcity)
                                team_field = request.form.get('teamfield')  # 可以为空
                                if str_None(team_field) is False:
                                    team_field = str_transfer(team_field)
                                    if not str.isalnum(team_field):
                                        return 'Please enter right 26 characters which can combine the numbers in team field name'
                                    else:
                                        print(team_field)

                                        team_rating = request.form.get('teamrating')  # 若位空则初始值则为0
                                        print(team_rating)
                                        if str_None(team_rating):
                                            team_rating = 0
                                            print(team_rating)
                                        combine_local = team_state + teamcity + team_field
                                        # print(combine_local)

                                        league_name = request.form.get('leaguename')
                                        if str_None(league_name):
                                            return 'The league name cannot be null.'
                                        else:
                                            league_name = str_transfer(league_name)
                                            if not str.isalnum(league_name):
                                                return 'Please enter right 26 characters which can combine the numbers in league name'
                                            else:
                                                # print(league_name)
                                                print(team_name, team_state, teamcity, team_field, team_rating,
                                                      league_name, combine_local)  # 🌹
                                                db_result = link_team_input(league_name, team_name, team_state,
                                                                            teamcity,
                                                                            team_field, team_rating)
                                                if db_result == "Team created":
                                                    result = str(db_result)
                                                    return render_template('add_new_team.html', error='', result=result)
                                                else:
                                                    error = str(db_result)
                                                    return render_template('add_new_team.html', error=error, result='')

    return render_template('add_new_team.html')


# Task 2 seasoninput ✅
@entry_input.route('/add_new_season', methods=['GET', 'POST'])
def season_input():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                season_name = request.form.get('seasonname')
                if str_None(season_name):
                    return 'The season name cannot be null.'
                else:
                    # print(season_name)
                    season_begin_date = request.form.get('seasonbegindate')
                    if str_None(season_begin_date):
                        return 'The season begin date can not be null.'
                    else:
                        # print(season_begin_date)
                        season_end_date = request.form.get('seasonenddate')
                        if str_None(season_end_date):
                            return 'The season end date can not be null'
                        else:
                            if season_end_date <= season_begin_date:
                                return "season end date should be later than season begin date"
                            else:
                                season_begin_date = date_transfer(season_begin_date)
                                season_end_date = date_transfer(season_end_date)
                                # print(season_end_date)
                                season_state = request.form.get('seasonstate')
                                if str_None(season_state):
                                    return 'The seasonstate cannot be null.'
                                else:
                                    season_state = str_transfer(season_state)
                                    if not str.isalnum(season_state):
                                        return 'Please enter right 26 characters which can combine the numbers in season state.'
                                    else:
                                        # print(season_state)
                                        season_city = request.form.get('seasoncity')
                                        if str_None(season_city):
                                            return 'The season city can not be null.'
                                        else:
                                            season_city = str_transfer(season_city)
                                            if not str.isalnum(season_city):
                                                return 'Please enter right 26 characters which can combine the numbers in season city.'
                                            else:
                                                # print(season_city)
                                                season_field = request.form.get('seasonfield')
                                                if str_None(season_field):
                                                    return 'The season field can not be null.'
                                                else:
                                                    season_field = str_transfer(season_field)
                                                    if not str.isalnum(season_field):
                                                        return 'Please enter right 26 characters which can combine the numbers in season field.'
                                                    else:
                                                        db_result = link_season_input(league_name, season_name,
                                                                                      season_begin_date,
                                                                                      season_end_date, season_state,
                                                                                      season_city,
                                                                                      season_field)
                                                        if db_result == 'Season created':
                                                            result = str(db_result)
                                                            return render_template('add_new_season.html', error='',
                                                                                   result=result)
                                                        else:
                                                            error = str(db_result)
                                                            return render_template('add_new_season.html', error=error,
                                                                                   result='')
    return render_template('add_new_season.html')


# ✅
@entry_input.route('/add_new_game', methods=['GET', 'POST'])
def game_input():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                # print(league_nameb)
                season_name = request.form.get('seasonname')
                if str_None(season_name):
                    return 'The season name cannot be null.'
                else:
                    # print(season_name)
                    team_namea = request.form.get('teamnamea')
                    if str_None(team_namea):
                        return 'The team A name cannot be null.'
                    else:
                        team_namea = str_transfer(team_namea)
                        if not str.isalnum(team_namea):
                            return 'Please enter right 26 characters which can combine the numbers in team A name'
                        else:
                            # print(team_namea)
                            team_nameb = request.form.get('teamnameb')
                            if str_None(team_nameb):
                                return 'The team B name cannot be null.'
                            else:
                                team_nameb = str_transfer(team_nameb)
                                if not str.isalnum(team_namea):
                                    return 'Please enter right 26 characters which can combine the numbers in team B name'
                                else:
                                    if team_namea == team_nameb:
                                        return 'Team can not play a game with themselves'
                                    game_date = request.form.get('gamedate')
                                    # print(game_date)
                                    if str_None(game_date):
                                        return 'The game date cannot be null.'
                                    else:
                                        game_date = date_transfer(game_date)
                                        # print(game_date)
                                        print(league_name, season_name, team_namea,
                                              team_nameb, game_date)  # 🌹
                                        db_result = link_game_input(league_name, season_name, team_namea, team_nameb,
                                                                    game_date)
                                        if db_result == "Game created":
                                            result = str(db_result)
                                            return render_template('add_new_game.html', error='', result=result)
                                        else:
                                            error = str(db_result)
                                            return render_template('add_new_game.html', error=error, result='')
    return render_template("add_new_game.html")


# Task 3 result ✅
@entry_input.route('/add_result', methods=['GET', 'POST'])
def result_input():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The league name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                # print(league_name)
                # print(league_nameb)
                season_name = request.form.get('seasonname')
                if str_None(season_name):
                    return 'The season name cannot be null.'
                else:
                    # print(season_name)
                    team_namea = request.form.get('teamnamea')
                    if str_None(team_namea):
                        return 'The team A name cannot be null.'
                    else:
                        team_namea = str_transfer(team_namea)
                        if not str.isalnum(team_namea):
                            return 'Please enter right 26 characters which can combine the numbers in team A name'
                        else:
                            # print(team_nameb)
                            team_nameb = request.form.get('teamnameb')
                            if str_None(team_nameb):
                                return 'The team B name cannot be null.'
                            else:
                                team_nameb = str_transfer(team_nameb)
                                if not str.isalnum(team_namea):
                                    return 'Please enter right 26 characters which can combine the numbers in team B name'
                                else:
                                    # print(team_nameb)
                                    score_a = request.form.get('scorea')
                                    if str_None(score_a):
                                        return 'The score A cannot be null.'
                                    else:
                                        # print(score_a)
                                        score_b = request.form.get('scoreb')
                                        if str_None(score_b):
                                            return 'The score B cannot be null.'
                                        else:
                                            # print(score_b)
                                            game_date = request.form.get('gamedate')
                                            # print(game_date)
                                            if str_None(game_date):
                                                return 'The game date cannot be null.'
                                            else:
                                                game_date = date_transfer(game_date)
                                                # print(game_date)
                                                print(league_name, season_name, team_namea,
                                                      team_nameb, score_a, score_b, game_date)  # 🌹
                                                db_result = link_result_input(league_name, season_name, team_namea,
                                                                              team_nameb, score_a, score_b,
                                                                              game_date)
                                                if db_result == "Score added":
                                                    result = str(db_result)
                                                    return render_template('add_result.html', error='', result=result)
                                                else:
                                                    error = str(db_result)
                                                    return render_template('add_result.html', error=error, result='')

    return render_template('add_result.html')
