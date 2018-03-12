import random
import time

#64-team tournament ~.75 seconds

class Team:
    def __init__(self, n, s, wl, kp, sos, wp_last_seven, luck, win_margin):
        self.__name = n
        self.__seed = s
        self.__games_won = 0
        self.__upsets = 0
        self.__teams_upset = []

        self.__kenpom_rank = kp
        self.__win_loss_percentage = wl
        self.__strength_of_schedule = sos
        self.__win_percentage_last_seven = wp_last_seven
        self.__luck = luck
        self.__win_margin = win_margin

    def get_name(self):
        return self.__name

    def get_seed(self):
        return self.__seed

    def get_kenpom_rank(self):
        return self.__kenpom_rank

    def get_win_loss_percentage(self):
        return self.__win_loss_percentage

    def get_strength_of_schedule(self):
        return self.__strength_of_schedule
    
    def get_win_percentage_last_seven(self):
        return self.__win_percentage_last_seven

    def get_luck(self):
        return self.__luck

    def get_win_margin(self):
        return self.__win_margin

    def set_upsets(self):
        self.__upsets += 1

    def add_team_upset(self, team_name):
        self.__teams_upset.append(team_name)

def tournament():
    print("2016 NCAA Tournament:")
    num_teams_left = len(teams)
    while num_teams_left > 1:
        print_round_message(num_teams_left)
        tournament_round()
        num_teams_left = len(teams)
        simulation_summary()
        print("####################################################################\n####################################################################\n####################################################################\n")      

def tournament_round():
    round_winners = []
    for x in range(0, len(teams) - 1, 2):
        round_winners.append(game(teams[x], teams[x + 1]))

    remove_losers(round_winners)

def game(team_one, team_two):
    winner = False
    team_one_greater = False
    win_likelihood = calculate_win_likelihood(team_one, team_two)

    if win_likelihood > 0:
        team_one_greater = True

    #print(win_likelihood, team_one.get_name(), team_two.get_name())
    win_likelihood = abs(win_likelihood) + 0.5
    win_likelihood = float("{0:.4f}".format(win_likelihood))

    if win_likelihood >= 1:
        win_likelihood = 0.9999
    elif win_likelihood < 0:
        win_likelihood = 0
    else:
        win_likelihood = win_likelihood * 10000

    print(win_likelihood, random.randint(0, 10000))

    winner = random.randint(0, 10000) < win_likelihood
    if team_one_greater and winner or not team_one_greater and not winner:
        return [team_one, team_two]
    else:
        return [team_two, team_one]

def calculate_win_likelihood(team_one, team_two):
    rank_difference = team_two.get_kenpom_rank() - team_one.get_kenpom_rank()
    win_percentage_difference = team_one.get_win_loss_percentage() - team_two.get_win_loss_percentage()
    schedule_strength_difference = (team_one.get_strength_of_schedule() + team_one.get_win_margin() / 2) / 2 - (team_two.get_strength_of_schedule() + team_two.get_win_margin() / 2) / 2
    recent_win_percentage_difference = team_one.get_win_percentage_last_seven() - team_two.get_win_percentage_last_seven()
    luck_difference = team_two.get_luck() - team_one.get_luck()

    return (adjust_rank_difference(rank_difference) * 0.65 + adjust_win_percentage_difference(win_percentage_difference) * 0.22 + adjust_schedule_strength_difference(schedule_strength_difference) * 0.09 + adjust_recent_win_percentage(recent_win_percentage_difference) * 0.04 + luck_difference * 0.5) / 2

def adjust_rank_difference(rank_difference):
    absolute_difference = abs(rank_difference)
    adjusted_difference = -(10 / (absolute_difference + 9.5238)) + 1.05

    if rank_difference < 0:
        return -1 * adjusted_difference
    else:
        return adjusted_difference

def adjust_win_percentage_difference(win_percentage_difference):
    absolute_difference = abs(win_percentage_difference)
    adjusted_difference = -(0.075 / (absolute_difference + 0.071428)) + 1.05

    if win_percentage_difference < 0:
        return -1 * adjusted_difference
    else:
        return adjusted_difference

def adjust_schedule_strength_difference(schedule_strength_difference):
    absolute_difference = abs(schedule_strength_difference)
    adjusted_difference = -(2.38 / (absolute_difference + 2.266667)) + 1.05

    if schedule_strength_difference < 0:
        return -1 * adjusted_difference
    else:
        return adjusted_difference
    
def adjust_recent_win_percentage(recent_win_percentage_difference):
    absolute_difference = abs(recent_win_percentage_difference)
    adjusted_difference = -(0.035 / (absolute_difference + 0.035)) + 1

    if recent_win_percentage_difference < 0:
        return -1 * adjusted_difference
    else:
        return adjusted_difference

def remove_losers(winner_array):
    for winner in winner_array:
        if winner[0].get_seed() > winner[1].get_seed():
            print("UPSET ALERT: no. ", winner[0].get_seed(), winner[0].get_name(), "beat no.", winner[1].get_seed(), winner[1].get_name())
            winner[0].set_upsets()
            winner[0].add_team_upset(winner[1].get_name())
        else:
            print(winner[0].get_name(), winner[0].get_seed())
        teams.remove(winner[1])

def print_round_message(num_teams):
    if num_teams == 16:
        print("Sweet Sixteen")
    elif num_teams == 8:
        print("Elite Eight")
    elif num_teams == 4:
        print("Final Four")
    elif num_teams == 2:
        print("National Championship Game")

#Simulation statistics
roundone     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundtwo     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundthree   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundfour    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
championship = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
winner       = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rounds       = [roundone, roundtwo, roundthree, roundfour, championship, winner]

winning_teams = {}

arizona_state = Team('Arizona State', 11, 20/31, 45, 5.8, 2/7, -0.072, 8.2)
syracuse = Team('Syracuse', 11, 20/33, 54, 8.72, 3/7, 0.007, 3.0)
saint_bonaventure = Team('St. Bonaventure', 11, 25/32, 69, 2.2, 6/7, 0.077, 6.9)
ucla = Team('UCLA', 11, 21/32, 48, 6.91, 4/7, -0.019, 5.6)

north_carolina_central = Team('NC Central', 16, 19/34, 309, -12.75, 5/7, 0.017, 3.3)
texas_southern = Team('Texas Southern', 16, 15/34, 249, -6.74, 7/7, -0.009, -2.0)
liu_brooklyn = Team('LIU Brooklyn', 16, 18/34, 251, -8.39, 5/7, 0.015, 0.9)
radford = Team('Radford', 16, 22/34, 170, -4.43, 7/7, 0.044, 3.0)

first_play_in = game(arizona_state, syracuse)[0]
second_play_in = game(saint_bonaventure, ucla)[0]
third_play_in = game(north_carolina_central, texas_southern)[0]
fourth_play_in = game(liu_brooklyn, radford)[0]

print(first_play_in.get_name())
print(second_play_in.get_name())
print(third_play_in.get_name())
print(fourth_play_in.get_name())

def fill_teams():
    return [Team('Virginia', 1, 31/33, 1, 9.99, 7/7, 0.032, 14.2), Team('UMBC', 16, 24/34, 184, -5.63, 6/7, 0.145, 4.4), 
            Team('Creighton', 8, 21/32, 27, 9.23, 3/7, -0.018, 10.1), Team('Kansas State', 9, 22/33, 44, 9.2, 4/7, 0.056, 4.5),
            Team('Kentucky', 5, 24/34, 18, 11.17, 6/7, -0.001, 6.5), Team('Davidson', 12, 21/32, 43, 1.88, 6/7, -0.051, 9.1), 
            Team('Arizona', 4, 27/34, 21, 6.33, 6/7, -0.072, 9.7), Team('Buffalo', 13, 26/34, 77, -1.02, 6/7, -0.005, 8.9),
            Team('Miami', 6, 22/31, 36, 8.17, 4/7, 0.034, 6.1), Team('Loyola-Chicago', 11, 28/33, 41, 0.07, 7/7, 0.058, 10.2), 
            Team('Tennessee', 3, 25/33, 11, 11.62, 6/7, 0.04, 8.2), Team('Wright State', 14, 25/34, 135, -4.78, 6/7, 0.056, 6.4), 
            Team('Nevada', 7, 27/34, 24, 4.45, 5/7, -0.028, 10.2), Team('Texas', 10, 19/33, 39, 11.77, 4/7, -0.018, 3.5), 
            Team('Cincinnati', 2, 30/34, 4, 3.18, 7/7, -0.004, 17.8), Team('Georgia State', 15, 24/10, 96, -2.79, 5/7, -0.022, 7.9),

            Team('Xavier', 1, 28/33, 14, 9.62, 5/7, 0.109, 9.8), third_play_in, 
            Team('Missouri', 8, 20/32, 38, 9.6, 3/7, -0.021, 5.2), Team('Florida State', 9, 20/31, 35, 7.99, 3/7, -0.032, 7.3),
            Team('Ohio State', 5, 24/32, 15, 8.16, 4/7, 0.027, 9.1), Team('South Dakota State', 12, 28/34, 75, -0.10, 7/7, 0.111, 10.8), 
            Team('Gonzaga', 4, 30/34, 8, 0.95, 7/7, -0.006, 17.4), Team('UNC Greensboro', 13, 27/34, 82, -4.99, 6/7, -0.011, 11.1),
            Team('Houston', 6, 26/33, 17, 3.39, 5/7, -0.009, 12.9), Team('San Diego State', 11, 22/32, 50, 3.37, 7/7, -0.015, 9.6), 
            Team('Michigan', 3, 28/35, 10, 8.78, 7/7, 0.037, 10.9), Team('Montana', 14, 26/33, 71, -2.18, 6/7, -0.005, 9.4), 
            Team('Texas A&M', 7, 20/32, 30, 11.34, 3/7, -0.007, 5.2), Team('Providence', 10, 21/34, 63, 10.42, 4/7, 0.088, 1.0), 
            Team('UNC', 2, 25/35, 7, 14.05, 4/7, -0.019, 8.9), Team('Lipscomb', 15, 23/32, 165, -4.94, 7/7, 0.114, 5.1),

            Team('Villanova', 1, 30/34, 2, 10.23, 6/7, -0.018, 16.2), fourth_play_in, 
            Team('Virginia Tech', 8, 21/32, 32, 8.18, 3/7, -0.003, 8.0), Team('Alabama', 9, 19/34, 51, 11.03, 2/7, 0, 2.4),
            Team('West Virginia', 5, 24/34, 13, 10.48, 5/7, -0.009, 10.6), Team('Murray State', 12, 26/31, 59, -4.19, 7/7, -0.013, 13.4), 
            Team('Wichita State', 4, 25/32, 20, 5.55, 5/7, -0.015, 16.3), Team('Marshall', 13, 24/34, 114, -1.67, 5/7, 0.04, 5.4),
            Team('Florida', 6, 20/32, 23, 10.74, 3/7, -0.049, 6.6), second_play_in, 
            Team('Texas Tech', 3, 24/33, 12, 9.26, 2/7, -0.021, 10.5), Team('Stephen F Austin', 14, 28/34, 111, -7.58, 6/7, 0.037, 13.0), 
            Team('Arkansas', 7, 23/34, 37, 10.15, 4/7, 0.062, 5.6), Team('Butler', 10, 20/33, 25, 10.58, 3/7, -0.037, 6.3), 
            Team('Purdue', 2, 28/34, 5, 8.55, 5/7, 0.003, 15.5), Team('Cal State Fullerton', 15, 20/31, 153, -1.28, 5/7, 0.089, 3.2), 
            
            Team('Kansas', 1, 27/34, 9, 11.49, 6/7, 0.06, 10.6), Team('Penn', 16, 24/32, 127, -4.63, 6/7, 0.078, 7.9), 
            Team('Seton Hall', 8, 21/32, 26, 9.58, 4/7, -0.02, 5.7), Team('NC State', 9, 21/32, 42, 7.64, 5/7, 0.007, 6.8),
            Team('Clemson', 5, 23/32, 19, 9.76, 3/7, 0.004, 7.5), Team('New Mexico State', 12, 28/33, 55, -1.51, 6/7, 0.032, 12.1), 
            Team('Auburn', 4, 25/32, 16, 7.53, 3/7, -0.012, 10.1), Team('Charleston', 13, 26/33, 120, -4.61, 6/7, 0.049, 6.3),
            Team('TCU', 6, 21/32, 22, 9.82, 4/7, -0.058, 7.1), first_play_in, 
            Team('Michigan State', 3, 29/33, 6, 6.5, 6/7, 0.048, 16.2), Team('Bucknell', 14, 25/34, 100, -4.85, 7/7, 0.02, 8.3), 
            Team('Rhode Island', 7, 25/32, 49, 2.69, 4/7, 0.037, 8.6), Team('Oklahoma', 10, 18/31, 47, 11.96, 2/7, 0.005, 3.5), 
            Team('Duke', 2, 26/33, 3, 10.9, 5/7, -0.029, 15.1), Team('Iona', 15, 20/33, 134, -2.39, 4/7, -0.022, 3.7)] #all the teams go in here from top to bottom, left to right

def simulation_summary():
    teams_left = len(teams)
    active_round = 0
    if teams_left == 32:
        active_round = 1
    elif teams_left == 16:
        active_round = 2
    elif teams_left == 8:
        active_round = 3
    elif teams_left == 4:
        active_round = 4
    elif teams_left == 2:
        active_round = 5
    else:
        active_round = 6
        if teams[0].get_name() in winning_teams:
            winning_teams[teams[0].get_name()] += 1            
        else:
            winning_teams[teams[0].get_name()] = 1
    for team in teams:
        rounds[active_round - 1][team.get_seed() - 1] += 1 

teams = fill_teams()
for x in range(0, 1000):
    teams = fill_teams()
    print("TOURNAMENT NO. ", x + 1)
    tournament()
    print('\n\n\n\n\n\n\n\n\n\n')

print(rounds[0])
print(rounds[1])
print(rounds[2])
print(rounds[3])
print(rounds[4])
print(rounds[5])
for key, value in winning_teams.items():
    print(key, value)
