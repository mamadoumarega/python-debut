import random

print("Winning Rules of Color choice Game as follows: " + "\nEnter a number from one two five and match computer "
                                                          "choice to wish")
computer_score = 0
player_score = 0

while True:
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 n\ntake a turn: ")

    # take a input
    player_choice = int(input("User turn: "))

    # OR is the short_circuit operator if any one is the condition is true then it turn True value

    # Looping until user enter invalid input
    while 5 < player_choice < 1:
        player_choice = int(input("enter valid input: "))

    # initialize value of choice col variable
    # corresponding to the player_choice value
    if player_choice == 1:
        choice_col = 'red'
    elif player_choice == 2:
        choice_col = 'yellow'
    elif player_choice == 3:
        choice_col = 'orange'
    elif player_choice == 4:
        choice_col = 'green'
    else:
        choice_col = 'blue'

    # print  user choice
    print("user color choice is: " + choice_col)
    print("\nNow its computer turn to choose a color................")

    # computer chooses randomly any number
    # among 1 , 2 and 3. Using method of random
    computer_choice = random.randint(1, 5)

    # looping until comp_choice value
    if computer_choice == 1:
        computer_choice_col = 'red'
    elif computer_choice == 2:
        computer_choice_col = 'yellow'
    elif computer_choice == 3:
        computer_choice_col = 'orange'
    elif computer_choice == 4:
        computer_choice_col = 'green'
    else:
        computer_choice_col = 'blue'

    print("Computer color choice is: " + computer_choice_col)

    # condition of winning
    if choice_col == computer_choice_col:
        player_score += 1
        print("player_score: " + str(player_score))
        print("computer_score: " + str(computer_score))
    else:
        computer_score += 1

    print("Do you want to play again? (Y/N)")
    answer = input()

    if answer == 'n' or answer == 'N':
        break
