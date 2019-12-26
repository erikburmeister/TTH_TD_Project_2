import csv
import random


def create_list_of_players(experience):
    with open('_soccer_players.csv', mode='r', newline='') as csv_file:
        data = csv.DictReader(csv_file)
        rows = list(data)

        completed_list_of_players = []

        for row in rows:
            if row['Soccer Experience'] == experience:
                player_info_list = []
                player_info_list.append(row['Name'])
                player_info_list.append(row['Soccer Experience'])
                player_info_list.append(row['Guardian Name(s)'])
                completed_list_of_players.append(player_info_list)

    random.shuffle(completed_list_of_players)
    return completed_list_of_players


def team_generator(list_1, list_2):
    experienced_players = list_1
    inexperienced_players = list_2

    sharks_team = []
    dragons_team = []
    raptors_team = []
    
    for shark in experienced_players[:]:
        if len(sharks_team) != 3:
            sharks_team.append(shark)
            if shark in experienced_players:
                experienced_players.pop(0)

    for shark in inexperienced_players[:]:
        if len(sharks_team) != 6:
            sharks_team.append(shark)
            if shark in inexperienced_players:
                inexperienced_players.pop(0)

    for dragon in experienced_players[:]:
        if len(dragons_team) != 3:
            dragons_team.append(dragon)
            if dragon in experienced_players:
                experienced_players.pop(0)

    for dragon in inexperienced_players[:]:
        if len(dragons_team) != 6:
            dragons_team.append(dragon)
            if dragon in inexperienced_players:
                inexperienced_players.pop(0)

    for raptor in experienced_players[:]:
        if len(raptors_team) != 3:
            raptors_team.append(raptor)
            if raptor in experienced_players:
                experienced_players.pop(0)

    for raptor in inexperienced_players[:]:
        if len(raptors_team) != 6:
            raptors_team.append(raptor)
            if raptor in inexperienced_players:
                inexperienced_players.pop(0)

    return sharks_team, dragons_team, raptors_team


def team_letter_generator(team, players, team_name):
        """
        Takes 3 arguments: 
        team(sharks_team), players(shark_names), and team_name(sharks).
        It will then generate a generic letter directed to the parents 
        of the player, with the.players name and team they have been 
        placed on. The title of the letter will be the name of the 
        player in lowercase and their name and last name will be 
        separated by an underscore as opposed to a space.
        """

        team = team
        players = players
        team_name = team_name

        n = 0

        for kid in team:
            with open(
            	'_'.join(players[n].lower().split())+'.txt', 'w'
            	) as file:

                n += 1

                file.write("""
                Dear {}, \n
                Your son/daughter {} will be part of the {}.
                The first practice session is scheduled for 
                Monday, March 18, 2019 \n
                Have an awesome Spring Break!
                Coach Erik \n""".format(kid[2], kid[0], team_name))


def teams_list_maker(team_1, team_2, team_3):
    """
    Generates a txt file with a list with 
    the team and players in the team.
    """

    sharks_team = team_1
    dragons_team = team_2
    raptors_team = team_3

    with open('teams.txt', 'w') as file:

        file.write('Sharks \n')
        file.write('====== \n')
        for shark in sharks_team:
            file.write(''.join(shark) + '\n')

        file.write('\n')
        file.write('Dragons \n')
        file.write('======= \n')
        for dragon in dragons_team:
            file.write(''.join(dragon) + '\n')

        file.write('\n')
        file.write('Raptors \n')
        file.write('======= \n')
        for raptor in raptors_team:
            file.write(''.join(raptor) + '\n')


def complete_team():
    list_of_teams = list(
    	team_generator(
    		create_list_of_players("YES"),
    		create_list_of_players("NO")
    		)
    	)

    shark_team = list_of_teams[0]
    dragon_team = list_of_teams[1]
    raptor_team = list_of_teams[2]

    shark_names = []
    dragon_names = []
    raptor_names = []

    sharks = 'Sharks'
    dragons = 'Dragons'
    raptors = 'Raptors'

    for kid in shark_team:
        shark_names.append(kid[0])

    for kid in dragon_team:
        dragon_names.append(kid[0])

    for kid in raptor_team:
        raptor_names.append(kid[0])

    team_letter_generator(shark_team, shark_names, sharks)
    team_letter_generator(dragon_team, dragon_names, dragons)
    team_letter_generator(raptor_team, raptor_names, raptors)
    teams_list_maker(shark_names, dragon_names, raptor_names)


def league_builder():
    complete_team()
    print("The team roster and parent letters have been generated successfully.")


if __name__ == '__main__':
    league_builder()
