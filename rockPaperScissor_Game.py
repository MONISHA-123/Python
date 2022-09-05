import random

def ExitGame():
    exit= input("\n If you want to exit, please enter 'E' ").lower()
    if(exit!='e'):
        Game()



def Game():
    print("""\nRules:
    \n Total number of round is 10
    \nIn every round u have to pick either of Rock/Scissor/Paper
    and computer will make his own choice.
    For each win the player will score 5 points and same for computer.
    \n To quit the game please enter "Q" to quit
    """)
    print("\n Lets Start the game!!!!!!!!!!!")
    choice=""
    computerPoints,playerPoints=0,0
    roundCount=1
    while(choice != 'q' and roundCount<=10):
        print("\nROUND ",roundCount)
        choice=input("Pick any one in 'Rock/Paper/Scissor'  or 'Q' to quit - ").lower()
        if(choice != "q"):
            computerChoice=random.choice(['rock','paper','scissor'])
            print("Computer Choice is ",computerChoice)
            if(choice == 'rock' or choice == 'paper' or choice == 'scissor'):
                if((choice=='rock' and computerChoice == 'scissor' ) or (choice =='paper' and computerChoice =='rock') or (choice=='scissor' and computerChoice =='paper')):
                    playerPoints+=5
                elif((computerChoice=='rock' and choice == 'scissor' ) or (computerChoice =='paper' and choice =='rock') or (computerChoice=='scissor' and choice =='paper')):
                    computerPoints+=5
            elif(choice != 'q'):
                roundCount-=1
                print("\n Input is not valid.")
            print("your Points",playerPoints)
            print("Computer's Points",computerPoints)
            roundCount+=1
    if(choice == 'q'):
        ExitGame()
    else:
        if(playerPoints<computerPoints):
            print("\nSorry! Better Luck Next Time")

        elif(playerPoints>computerPoints):
            print("\n Congrats! Its a great Win")
        else:
            if(computerPoints != 0 and playerPoints !=0):
                print("\n Its a Draw!") 

        startGame=input("\n Can we start playing again? ").lower()
        if(startGame == 'yes'):
            Game()
        else:
            ExitGame()



print("Welcome to Rock Paper Scissor game!")
startGame=input("\n Can we start playing?  ").lower()
if(startGame == 'yes'):
    Game()
else:
    ExitGame()
