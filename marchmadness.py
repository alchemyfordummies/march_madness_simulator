import random
import time

#64-team tournament ~.75 seconds

class Team:
    def __init__(self, n, s):
        self.__name = n;
        self.__seed = s;
        self.__games_won = 0;
        self.__upsets = 0;
        self.__teams_upset = [];

    def get_name(self):
        return self.__name

    def get_seed(self):
        return self.__seed

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
    if team_one.get_seed() == team_two.get_seed():
        winner = (random.randint(0, 100) < 50)
    else:
        winner = random.randint(0, 1000) < matchups[team_one.get_seed() - 1][team_two.get_seed() - 1]

    if (winner):
        return [team_one, team_two]
    else:
        return [team_two, team_one]

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

#Tournament setup
                #1   #2   #3   #4   #5   #6   #7   #8   #9   #10  #11  #12  #13  #14  #15  #16
seedone      = [500, 528, 606, 686, 840, 687, 833, 805, 904, 857, 500, 993, 990, 890, 920, 999]
seedtwo      = [472, 500, 623, 444, 200, 722, 722, 444, 500, 600, 929, 955, 830, 860, 937, 920]
seedthree    = [394, 377, 500, 625, 500, 548, 600, 650, 950, 692, 708, 770, 800, 836, 965, 890]
seedfour     = [314, 556, 375, 500, 551, 333, 400, 300, 667, 940, 710, 684, 803, 800, 830, 860]
seedfive     = [160, 800, 500, 449, 500, 530, 530, 250, 333, 930, 680, 669, 800, 770, 990, 830]
seedsix      = [313, 278, 452, 667, 470, 500, 625, 250, 641, 600, 649, 680, 710, 875, 730, 800]
seedseven    = [167, 278, 400, 600, 470, 375, 500, 500, 641, 605, 110, 650, 680, 930, 667, 770]
seedeight    = [195, 556, 350, 700, 750, 750, 500, 500, 526, 560, 790, 310, 925, 680, 710, 740]
seednine     = [96,  500, 50,  333, 667, 359, 359, 474, 500, 530, 560, 590, 920, 650, 680, 710]
seedten      = [143, 400, 308, 60,  70,  400, 395, 440, 470, 500, 333, 560, 590, 710, 920, 680]
seedeleven   = [500, 71,  292, 290, 320, 351, 890, 210, 440, 667, 500, 530, 560, 890, 620, 650]
seedtwelve   = [7,   45,  230, 316, 331, 320, 350, 690, 410, 440, 470, 500, 727, 560, 590, 620]
seedthirteen = [10,  170, 200, 197, 200, 290, 320, 75,  80,  410, 440, 273, 500, 530, 560, 590]
seedfourteen = [110, 140, 164, 200, 230, 125, 70,  320, 350, 290, 110, 440, 470, 500, 530, 560]
seedfifteen  = [80,  63,  35,  170, 200, 230, 333, 290, 320, 80,  380, 410, 440, 470, 500, 530]
seedsixteen  = [1,   80,  110, 140, 170, 200, 230, 260, 290, 320, 350, 380, 410, 440, 470, 500]
matchups     = [seedone, seedtwo, seedthree, seedfour, seedfive, seedsix,
                seedseven, seedeight, seednine, seedten, seedeleven, seedtwelve,
                seedthirteen, seedfourteen, seedfifteen, seedsixteen]

#Simulation statistics
roundone     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundtwo     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundthree   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
roundfour    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
championship = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
winner       = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rounds       = [roundone, roundtwo, roundthree, roundfour, championship, winner]

winning_teams = {}

def fill_teams():
    return [Team('Villanova', 1), Team('MSM/UNO', 16), Team('Wisconsin', 8), Team('Virginia Tech', 9),
            Team('Virginia', 5), Team('UNC Wilmington', 12), Team('Florida', 4), Team('East Tennessee State', 13),
            Team('SMU', 6), Team('Providence/USC', 11), Team('Baylor', 3), Team('New Mexico State', 14), 
            Team('South Carolina', 7), Team('Marquette', 10), Team('Duke', 2), Team('Troy', 15),

            Team('Gonzaga', 1), Team('South Dakota St.', 16), Team('Northwestern', 8), Team('Vadnerbilt', 9),
            Team('Notre Dame', 5), Team('Princeton', 12), Team('West Virginia', 4), Team('Bucknell', 13),
            Team('Maryland', 6), Team('Xavier', 11), Team('Florida State', 3), Team('Florida Gulf Coast', 14), 
            Team('Saint Mary\s', 7), Team('VCU', 10), Team('Arizona', 2), Team('North Dakota', 15), 
            
            Team('Kansas', 1), Team('NC Central/UC Davis', 16), Team('Miami (FL)', 8), Team('Michigan St.', 9),
            Team('Iowa State', 5), Team('Nevada', 12), Team('Purdue', 4), Team('Vermont', 13),
            Team('Creighton', 6), Team('Rhode Island', 11), Team('Oregon', 3), Team('Iona', 14), 
            Team('Michigan', 7), Team('Oklahoma State', 10), Team('Louiseville', 2), Team('Jacksonville State', 15), 
            
            Team('UNC', 1), Team('Texas Southern', 16), Team('Arkansas', 8), Team('Seton Hall', 9),
            Team('Minnesota', 5), Team('Middle Tennessee State', 12), Team('Butler', 4), Team('Winthrop', 13),
            Team('Cincinnati', 6), Team('Kansas St./Wake Forest', 11), Team('UCLA', 3), Team('Kent State', 14), 
            Team('Dayton', 7), Team('Wichita State', 10), Team('Kentucky', 2), Team('Northern Kentucky', 15)] #all the teams go in here from top to bottom, left to right

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
'''
1
16
    1
    8
8
9
        1
        4
4
13
    4
    5
5
12
            1   
            2
2
15
    2
    7
7
10
        2
        3
3
14
    3
    6
6
11
'''
