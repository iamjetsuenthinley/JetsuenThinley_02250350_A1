import random

def rock_logic(cc): #'cc' refers to as computer choice
    if cc=='r':
        print("Computer chose rock. It's a Draw!")
    elif cc=='p':
        print("Computer chose papers. You Lose!")
    else:print("Computer chose scissors. You Win!")

def paper_logic(cc): #'cc' refers to as computer choice
    if cc=='r':
        print("Computer chose rock. You Win!")
    elif cc=='p':
        print("Computer chose paper. It's a Draw!")
    else:print("Computer chose scissors. You Lose!")

def scissors_logic(cc): #'cc' refers to as computer choice
    if cc=='r':
        print("Computer chose rock. You Lose!")
    elif cc=='p':
        print("Computer chose paper. You Won!")
    else:print("Computer chose scissors. It's a Draw!")

'''The def function above is for the 2nd game. On what 'r','p' or 'c' results to '''

def ask_another_round(): ###ask if User wants to go another round
    while True:
        choice2=input("\nWould you like to go another round?(y/n): ").lower()
        if choice2=='y':
            return True
        elif choice2=='n':
            return False
        else:print("Enter valid descision\n")
    

#########__________MAIN___________##############
running=True
while running:
    '''running will remain True until user enters '3' to Exit the program.'''
    while True:
        print("MENU")
        print("1. Guess Number Game\n2. Rock Paper Scissors Game\n3. Exit Program\n")
        choice=input("Select a Game(1-2): ")

        if choice=='1':
            game1_running=True
            '''game1_ruuning will remain true unless user decides not to go another round. 
            Hence Going back to GAME MENU'''
            while game1_running:
                print("I'm thinking of a number between 1 and 100...")
                guess_done=False
                while not guess_done:
                    num=random.randint(1,100)
                    try:
                        while True:
                            user_guess=int(input("\nGuess The Number: "))
                            if user_guess in range(1,101):
                                if user_guess>num:
                                    diff=user_guess-num
                                    if diff>=10:
                                        print("Too High! Try Again.")
                                    elif diff in range(3,10):
                                        print("Quite High! Try Again")
                                    else: 
                                        print("Very Close but High! Try Again")
                                elif user_guess<num: 
                                    diff=num-user_guess
                                    if diff>=10:print("Too Low! Try Again.")
                                    elif diff in range(3,10):
                                        print("Quite Low! Try Again")
                                    else: print("Very Close but Low! Try Again")
                                elif user_guess==num:
                                    print(f"{num} is correct, Congratulations!!!\n")
                                    if not ask_another_round():
                                        guess_done=True
                                        game1_running=False
                                        break
                                    else:
                                        guess_done=False
                                        break
                            else:print("Choose number from(1-100)")
                    except:
                        print("choose a valid number")

        elif choice=='2':
            print("You are up againt a a computer's random function")
            game2_running=True
            '''game2_running will remain True unless user decides not to go another round.'''
            while game2_running:
                picks=['r','p','s']
                com=random.choice(picks)
                print("ENTER 'r' FOR ROCK/ 'p' FOR PAPER/ 's' for scissors")
                rps=input("Enter your pick: ")
                if rps=='r':
                    rock_logic(com)   #com refers to computer's pick
                    if not ask_another_round():
                        break
                elif rps=='p':
                    paper_logic(com)
                    if not ask_another_round():
                        break
                elif rps=='s':
                    scissors_logic(com)
                    if not ask_another_round():
                        break
                else:
                    print("Chose a from 'r'(Rock), 'p'(Paper), 's'(Scissors)")
        
        elif choice=='3':       
            print("Exiting Program...")
            running=False
            break
        
        else:print("Enter a choice from (1-3)\n")

               


