import random
import time
board=[["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
player1Points,player2Points=0,0
def displayBoard():
        time.sleep(1)
        for ele in board:
                print(*ele)
        print('*'*30)

def updateScore():
        player1Points,player2Points=0,0
        for i in range(3):
                if(board[i][0] ==  board[i][1]  and board[i][1] == board[i][2]):
                        if(board[i][0] == 'X'):
                                player1Points+=1
                        elif(board[i][0] == 'O'):
                                player2Points+=1
        for i in range(3):
                if(board[0][i] ==  board[1][i]  and board[1][i] == board[2][i]):
                        if(board[0][i] == 'X'):
                                player1Points+=1
                        elif(board[0][i] == 'O'):
                                player2Points+=1
        if(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' ):
                player1Points+=1
        elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' ):
                player2Points+=1
        
        if(board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' ):
                player1Points+=1
        elif(board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' ):
                player2Points+=1
        print('*'*30)
        print("your Score ",player1Points)
        print("computer Score ",player2Points)
        print('*'*30)

        if(player1Points > player2Points):
                print('\n !!!You Won')
        elif(player2Points == player1Points):
                print("\n Its a Draw")
        else:
                print("Better Luck next time!")
                


def player2Game():
        while True:
                x=random.randint(0,2)
                y=random.randint(0,2)
                if(board[x][y] == '-'):
                        print("Computer's Choice is ",x,y,sep="")
                        break
        board[x][y]='O'
        displayBoard()

def player1Game():
        while True:
                x,y=map(int,list(input('Enter your position :')))
                if(board[x][y] == '-'):
                        board[x][y]='X'
                        break
                else:
                        print("!! The entered position is already occupied !!")
        displayBoard()


def startGame(value):
        
        if(value):
                player1Game()
        while(board[0][0] == '-' or board[0][1] == '-' or board[0][2] == '-' or board[1][0] == '-' or board[1][1] == '-' or board[1][2] == '-' or board[2][0] == '-' or board[2][1] == '-' or board[2][2] == '-' ):
                player2Game()
                player1Game()
        updateScore()
print( "lets Toss the coin to start the game!!!")
tossUserValue=input("Heads or tail? Enter 'H' for heads and 'T' for tail :")
tossRealvalue= random.choice(['h','t'])
if(tossUserValue.lower() == tossRealvalue):
        print('Great! You won the toss')
        startGame(1)
else:
        print('Sry u lost the toss, computer will be starting first')
        time.sleep(1)
        startGame(0)

