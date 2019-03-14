import csv
import random


def league_builder():
    
    def team_letter_generator(team, players, team_name):
        """Takes 3 arguments: team(sharks_team), players(shark_names), and team_name(sharks).
        It will then generate a generic letter directed to the parents of the player, with the
        players name and team they have been placed on.
        The title of the letter will be the name of the player in lowercase and their name and 
        last name will be separated by an underscore as opposed to a space.
        """
        
        n = 0

        for kid in team:
            with open('_'.join(players[n].lower().split())+'.txt', 'w') as file:
                n += 1

                file.write("""
                Dear {}, \n
                Your son/daughter {} will be part of the {}.
                The first practice session is scheduled for Monday, March 18, 2019 \n
                Have an awesome Spring Break!
                Coach Erik \n""".format(kid[2], kid[0], team_name))

                
    def teams_list_maker():
        """Generates a txt file with a list with the team and players in the team."""
        
        with open('teams.txt', 'w') as file:

            file.write('Sharks \n')
            file.write('====== \n')
            for shark in sharks_team:
                file.write(', '.join(shark) + '\n')

            file.write('\n')
            file.write('Dragons \n')
            file.write('======= \n')
            for dragon in dragons_team:
                file.write(', '.join(dragon) + '\n')

            file.write('\n')
            file.write('Raptors \n')
            file.write('======= \n')
            for raptor in raptors_team:
                file.write(', '.join(raptor) + '\n')
    
    
    # Opens CSV file and extracts info into multiple lists
    with open('soccer_players.csv', mode='r', newline='') as csv_file:
        data = csv.DictReader(csv_file)
        rows = list(data)

        completed_list_of_experienced_players = []
        completed_list_of_unexperienced_players = []

        for row in rows:
            if row['Soccer Experience'] == 'YES':
                player_info_list = []
                player_info_list.append(row['Name'])
                player_info_list.append(row['Soccer Experience'])
                player_info_list.append(row['Guardian Name(s)'])
                completed_list_of_experienced_players.append(player_info_list)

        for row in rows:
            if row['Soccer Experience'] == 'NO':
                player_info_list = []
                player_info_list.append(row['Name'])
                player_info_list.append(row['Soccer Experience'])
                player_info_list.append(row['Guardian Name(s)'])
                completed_list_of_unexperienced_players.append(player_info_list)

    
    # Randomizes lists to generate unique teams each time the program runs.
    random.shuffle(completed_list_of_experienced_players)
    random.shuffle(completed_list_of_unexperienced_players)


    # Fills teams with 3 experienced players and 3 unexperienced players each.
    sharks_team = []
    dragons_team = []
    raptors_team = []

    for shark in completed_list_of_experienced_players[:]:
        if len(sharks_team) != 3:
            sharks_team.append(shark)
            if shark in completed_list_of_experienced_players:
                completed_list_of_experienced_players.pop(0)

    for shark in completed_list_of_unexperienced_players[:]:
        if len(sharks_team) != 6:
            sharks_team.append(shark)
            if shark in completed_list_of_unexperienced_players:
                completed_list_of_unexperienced_players.pop(0)

    for dragon in completed_list_of_experienced_players[:]:
        if len(dragons_team) != 3:
            dragons_team.append(dragon)
            if dragon in completed_list_of_experienced_players:
                completed_list_of_experienced_players.pop(0)

    for dragon in completed_list_of_unexperienced_players[:]:
        if len(dragons_team) != 6:
            dragons_team.append(dragon)
            if dragon in completed_list_of_unexperienced_players:
                completed_list_of_unexperienced_players.pop(0)

    for raptor in completed_list_of_experienced_players[:]:
        if len(raptors_team) != 3:
            raptors_team.append(raptor)
            if raptor in completed_list_of_experienced_players:
                completed_list_of_experienced_players.pop(0)

    for raptor in completed_list_of_unexperienced_players[:]:
        if len(raptors_team) != 6:
            raptors_team.append(raptor)
            if raptor in completed_list_of_unexperienced_players:
                completed_list_of_unexperienced_players.pop(0)


    # Creates a list of only the names of the players in each team, 
    # and variables with a string of the team names. 
    shark_names = []
    dragon_names = []
    raptor_names = []
    
    sharks = 'Sharks'
    dragons = 'Dragons'
    raptors = 'Raptors'

    for kid in sharks_team:
        shark_names.append(kid[0])

    for kid in dragons_team:
        dragon_names.append(kid[0])

    for kid in raptors_team:
        raptor_names.append(kid[0])
        
    
    # Prints message as feedback to let the user know the program finished running. 
    print("The team roster and parent letters have been generated successfully.")
    
    
    # Executes functions.
    teams_list_maker()
    team_letter_generator(sharks_team, shark_names, sharks)
    team_letter_generator(dragons_team, dragon_names, dragons)
    team_letter_generator(raptors_team, raptor_names, raptors)

        
if __name__ == '__main__':
    league_builder()