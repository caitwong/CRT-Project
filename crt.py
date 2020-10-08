runProgram = True
while(runProgram):

    import random
    p1name = input('Input Player name: ')
    player_choice = int(input("Choose one: compost(1), recycling(2), or trash(3): "))

    computer_choice = random.randint(1, 4)

    print(p1name, 'choice: ', player_choice)
    print('Computer choice: ', computer_choice)

    outcome = ["You Win!", "Draw", "You Lose"]
    wins = 0

    if player_choice == computer_choice:
        print (outcome[1])
    elif player_choice == 1 and computer_choice == 2:
        print (outcome[0])
        wins += 1
    elif player_choice == 2 and computer_choice == 3:
        print (outcome[0])
        wins += 1
    elif player_choice == 3 and computer_choice == 1:
        print (outcome[0])
        wins += 1
    else:
        print (outcome[2])
    
    print('Wins: ', wins)
    
    again = input("Would you like to play again?")
    if again == "no":
        runProgram = False

