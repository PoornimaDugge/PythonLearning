from random import shuffle

my_list=[' ','O',' ']

def Player_game(my_list,guess):
    if my_list[guess]=='O' or my_list[guess]=='o':
        print("You win!!")
    else:
        print("You lost")

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess =''
    while guess not in ['0','1','2']:
        guess=input("Pick the number : 0 or 1 or 2:\n")

    return int(guess)

shuffle_list(my_list)
guess= player_guess()
Player_game(my_list,guess)






