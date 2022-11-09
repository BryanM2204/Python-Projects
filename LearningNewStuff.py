def player_dictionary(player_dict, player_list):
    for i in player_list:
        if i in player_dict:
            print(f'Jersey number: {i}, Rating: {player_dict[i]}')

def print_menu():
    allowed_character = ['a', 'd', 'u', 'r', 'o', 'q']
    menu = ('\nMENU\n'
            'a - Add player\n'
            'd - Remove player\n'
            'u - Update player rating\n'
            'r - Output players above a rating\n'
            'o - Output roster\n'
            'q - Quit\n'
            )
    print(menu)
    user_input = input('Choose an option:\n')
    if user_input in allowed_character:
        menu_function(user_input)
    else:
        print_menu()
    
    
        
def menu_function(user_input):
    if user_input == 'o':
        print('\nROSTER')
        player_dictionary(player_dict, player_list)
        print_menu()
    
    elif user_input == 'a':
        new_jersey = int(input('Enter a new player\'s jersey number:\n'))
        new_rating = int(input('Enter the player\'s rating:'))
        player_list.append(new_jersey)
        player_list.sort()
        player_dict[new_jersey] = new_rating
        
        print_menu()
        
    elif user_input == 'd':
        remove_jersey = int(input('Enter a jersey number:\n'))
        player_list.remove(remove_jersey)
        del player_dict[remove_jersey]
        print_menu()
        
    elif user_input == 'u':
        desired_jersey = int(input('Enter a jersey number:\n'))
        updated_rating = int(input('Enter a new rating for player:\n'))
        player_dict[desired_jersey] = updated_rating
        print_menu()
        
    elif user_input == 'r':
        minimum_rating = int(input('Enter a rating:\n'))
        print(f'ABOVE {minimum_rating}')
        for i in player_list:
            if player_dict[i] > minimum_rating:
                print(f'Jersey number: {i}, Rating: {player_dict[i]}')
        print_menu()
    
    elif user_input == 'q':
        exit()
        
player_dict = {}
player_list = []

player1_jersey = int(input('Enter player 1\'s jersey number:\n'))
player1_rating = int(input('Enter player 1\'s rating:\n'))
player_dict[player1_jersey] = player1_rating

player2_jersey = int(input('\nEnter player 2\'s jersey number:\n'))
player2_rating = int(input('Enter player 2\'s rating:\n'))
player_dict[player2_jersey] = player2_rating

player3_jersey = int(input('\nEnter player 3\'s jersey number:\n'))
player3_rating = int(input('Enter player 3\'s rating:\n'))
player_dict[player3_jersey] = player3_rating

player4_jersey = int(input('\nEnter player 4\'s jersey number:\n'))
player4_rating = int(input('Enter player 4\'s rating:\n'))
player_dict[player4_jersey] = player4_rating

player5_jersey = int(input('\nEnter player 5\'s jersey number:\n'))
player5_rating = int(input('Enter player 5\'s rating:\n'))
player_dict[player5_jersey] = player5_rating

player_list.extend((player1_jersey, player2_jersey, player3_jersey, player4_jersey, player5_jersey))
player_list.sort()

print('\nROSTER')
player_dictionary(player_dict, player_list)
print_menu()


