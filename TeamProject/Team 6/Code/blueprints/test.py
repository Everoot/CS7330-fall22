import blueprints.link_entryinput as lei
from bson import ObjectId
from app import db
import blueprints.link_app as la
import blueprints.link_entrydelete as led
import blueprints.link_entryquery as leq

print(lei.link_league_input("arnold", "mark", "3894018374"))


print(lei.link_season_input("arnold", "1", "20221110", "20221223", "ny", "newyorkcity", "nyfield"))
print(lei.link_season_input("arnold", "1", "20231110", "20231223", "tx", "dallas", "canvas"))



print(lei.link_team_input("arnold", "team1", "TX", "dallas", "canvas", "0"))
print(lei.link_team_input("arnold", "team2", "TX", "dallas", "canvas", "0"))
print(lei.link_team_input("arnold", "team3", "TX", "dallas", "canvas", "0"))
print(lei.link_team_input("arnold", "team4", "TX", "dallas", "canvas", "0"))
print(lei.link_team_input("arnold", "team5", "TX", "dallas", "canvas", "0"))


print(lei.link_game_input("arnold", "1", "team1", "team2", "20221110"))
print(lei.link_game_input("arnold", "1", "team1", "team3", "20221111"))
print(lei.link_game_input("arnold", "1", "team1", "team4", "20221112"))
print(lei.link_game_input("arnold", "1", "team2", "team3", "20221113"))
print(lei.link_game_input("arnold", "1", "team2", "team4", "20221114"))
print(lei.link_game_input("arnold", "1", "team3", "team4", "20221115"))
print(lei.link_result_input("arnold", "1", "team1", "team2", "3", "5", "20221110"))
print(lei.link_result_input("arnold", "1", "team1", "team3", "4", "2", "20221111"))
print(lei.link_result_input("arnold", "1", "team1", "team4", "3", "1", "20221112"))
print(lei.link_result_input("arnold", "1", "team2", "team3", "1", "1", "20221113"))
print(lei.link_result_input("arnold", "1", "team2", "team4", "7", "2", "20221114"))
print(lei.link_result_input("arnold", "1", "team3", "team4", "1", "6", "20221115"))

print(lei.link_game_input("arnold", "2", "team1", "team2", "20231110"))
print(lei.link_game_input("arnold", "2", "team1", "team3", "20231111"))
print(lei.link_game_input("arnold", "2", "team1", "team4", "20231112"))
print(lei.link_game_input("arnold", "2", "team2", "team3", "20231113"))
print(lei.link_game_input("arnold", "2", "team2", "team4", "20231114"))
print(lei.link_game_input("arnold", "2", "team3", "team4", "20231115"))
print(lei.link_result_input("arnold", "2", "team1", "team2", "3", "1", "20231110"))
print(lei.link_result_input("arnold", "2", "team1", "team3", "1", "5", "20231111"))
print(lei.link_result_input("arnold", "2", "team1", "team4", "2", "3", "20231112"))
print(lei.link_result_input("arnold", "2", "team2", "team3", "5", "2", "20231113"))
print(lei.link_result_input("arnold", "2", "team2", "team4", "3", "3", "20231114"))
print(lei.link_result_input("arnold", "2", "team3", "team4", "5", "4", "20231115"))

print(leq.link_league_champions_query("arnold"))
print(leq.link_league_basic_query("arnold"))

#print(lei.link_league_input("space", "Jo", "3894018370"))
#print(lei.link_season_input("space", "10", "20211110", "20211223", "tx", "dallas", "canvas"))
#print(lei.link_team_input("space", "team6", "TX", "dallas", "canvas", "0"))