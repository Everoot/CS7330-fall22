from flask import Flask, render_template, request, Blueprint

entry_modify = Blueprint("modify", __name__, url_prefix="/modify")  # 创建一个蓝图
from blueprints.link_entrymodify import link_update_input, link_move_team


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

def date_back(a):
    year = a[0:4]
    month = a[4:6]
    day = a[6:8]
    list = [year, month, day]
    a = '-'.join(list)
    return a

# Task 4 update ✅
@entry_modify.route('/modify_date', methods=['GET', 'POST'])
def update_input():
    if request.method == 'POST':
        update = request.form.get('update')
        if str_None(update):
            return 'The update date cannot be null.'
        else:
            update = date_transfer(update)
            print(update)                                # 🌹---------------
            db_result = link_update_input(update)
            if db_result == "Time updated":
                result = str(db_result)
                return render_template('modify_date.html', error='', result=result)
            else:
                error = "Sorry, update the current date fail."
                return render_template('modify_date.html', error=error, result='')
    return render_template('modify_date.html')


# ✅
@entry_modify.route('/modify_move_team', methods=['GET', 'POST'])
def move_team():
    if request.method == 'POST':
        move_team_name = request.form.get('moveteamname')
        if str_None(move_team_name):
            return 'The move team name cannot be null.'
        else:
            move_team_name = str_transfer(move_team_name)
            if not str.isalnum(move_team_name):
                return 'Please enter right 26 characters which can combine the numbers in move team name'
            else:
                league_name_future = request.form.get('leaguenamefuture')
                if str_None(league_name_future):
                    return 'The future league name cannot be null.'
                else:
                    league_name_future = str_transfer(league_name_future)
                    if not str.isalnum(league_name_future):
                        return 'Please enter right 26 characters which can combine the numbers in future league name'
                    else:
                        # print(league_name_future)
                        print(move_team_name,league_name_future)  # 🌹 ------------------------------------------------
                        db_result = link_move_team(move_team_name,league_name_future)
                        result = str(db_result)
                        return render_template('modify_move_team.html', error = '', result = result)
    return render_template('modify_move_team.html')


