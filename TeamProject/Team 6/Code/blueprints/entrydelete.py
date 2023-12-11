from flask import Flask, render_template, request, Blueprint
from blueprints.link_entrydelete import link_delete_team, link_delete_league
entry_delete = Blueprint("delete", __name__, url_prefix="/delete")  # 创建一个蓝图

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

# ✅

@entry_delete.route('/delete_team', methods=['GET', 'POST'])
def delete_team():
    if request.method == 'POST':

        team_name = request.form.get('teamname')
        if str_None(team_name):
            return 'The team name cannot be null.'
        else:
            team_name = str_transfer(team_name)
            if not str.isalnum(team_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(team_name)
                # ---------------------------------------------------------------
                db_result = link_delete_team(team_name)  # 🌹
                return render_template('delete_team.html', result=db_result)

    return render_template('delete_team.html')

#✅
@entry_delete.route('/delete_league', methods = ['GET', 'POST'])
def delete_league():
    if request.method == 'POST':
        league_name = request.form.get('leaguename')
        if str_None(league_name):
            return 'The team name cannot be null.'
        else:
            league_name = str_transfer(league_name)
            if not str.isalnum(league_name):
                return 'Please enter right 26 characters which can combine the numbers in league name'
            else:
                print(league_name)
                # ---------------------------------------------------------------
                db_result = link_delete_league(league_name)  # 🌹
                return render_template('delete_league.html', result=db_result)
    return  render_template('delete_league.html')

