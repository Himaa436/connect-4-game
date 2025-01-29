import sys
from PyQt6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget ,QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QMainWindow
from ui_form import Ui_Widget


s = "A B C D E F G\n"
arr = [
    list("O O O O O O O"),
    list("O O O O O O O"),
    list("O O O O O O O"),
    list("O O O O O O O"),
    list("O O O O O O O"),
    list("O O O O O O O")
]
a = [5,5,5,5,5,5,5]
t = 42
turn = 0

def Row_check(x , color):
    cnt=0
    score=0
    for i in range(0,13,2):
        if(arr[x][i]== color and score == 0):
            cnt += 1
        elif(arr[x][i]== color and score != 0):
            cnt += 1
            score+=1
        elif(arr[x][i]!= color ):
            cnt=0
        elif(arr[x][i]!= color and score!=0):
            return score
        if(cnt==4):
            score+=1
    return score

def col_check(x , color):
    cnt=0
    score=0
    for i in range(0,6,1):
        if(arr[i][x]== color and score == 0):
            cnt += 1
        elif(arr[i][x]== color and score != 0):
            cnt += 1
            score+=1
        elif(arr[i][x]!= color ):
            cnt=0
        elif(arr[i][x]!= color and score!=0):
            return score
        if(cnt==4):
            score+=1
    return score


def all_row(color):
    score=0
    for i in range(0,6):
        score+=Row_check(i,color)
    return score

def valid(x , y):
    if(x < 6 and y < 13 and x >= 0 and y >= 0):
        return True
    else:
        return False

def diagonal_check(x, y, color):
    cnt=0
    score=0
    
    while(valid(x , y)):
        
        if(arr[x][y]==color and score == 0):
            cnt += 1
        elif(arr[x][y]==color and score != 0):
            cnt += 1
            score+=1
        elif(arr[x][y]!=color):
            cnt=0
        elif(arr[x][y]!=color and score!=0):
            return score
        if(cnt==4):
            score+=1
        x += 1
        y += 2
    return score

def x_diagonal_check(x, y, color):
    cnt=0
    score=0
    
    while(valid(x , y)):
        if(arr[x][y]==color and score == 0):
            cnt += 1
        elif(arr[x][y]==color and score != 0):
            cnt += 1
            score+=1
        elif(arr[x][y]!=color):
            cnt=0
        elif(arr[x][y]!=color and score!=0):
            return score
        if(cnt==4):
            score+=1
        x += 1
        y -= 2
    return score

def all_x(color):
    score = 0
    for i in range(0,3):
        score += diagonal_check(i, 0 ,color)
    for j in range(2,7,2): # todoooooooooooo
        score += diagonal_check(0, j ,color)
    for i in range(0,3):
        score += x_diagonal_check(i, 12 ,color)
    for j in range(6,11,2):
        score += x_diagonal_check(0, j ,color)

    return score


def all_col(color):
    score=0
    for i in range(0,13,2):
        score+=col_check(i, color)
    return score

def check(color):
    return all_col(color) + all_row(color) + all_x(color)


Y_Score=0 
R_Score=0
while (t>0):
    
    print(f"Y Score is {check('Y')} \t and \t R Score is {check('R')} \n")
    print(s)
    for i in arr:
        print(''.join(i))
    
    player = "Yellow"
    if(turn % 2 == 0):
        player = "Yellow"
    else:
        player = "Red"
    print(f"{player} player turn: ")
    x = input()
    if((x=='A' or x=='a') and turn%2==0):
        arr[a[0]][2*0]='Y'
        turn += 1
        
        #Y_Score check_y(a[0],0)
        a[0] -= 1
    elif((x=='A' or x=='a') and turn%2==1):
        arr[a[0]][2*0]='R'
        turn += 1
        
        #R_Score check_r(a[0],0)
        a[0] -= 1
    elif((x=='B' or x=='b') and turn%2==0):
        arr[a[1]][2*1]='Y'
        turn += 1
        
        #Y_Score check_y(a[1],2)
        a[1] -= 1
    elif((x=='B' or x=='b') and turn%2==1):
        arr[a[1]][2*1]='R'
        turn += 1
        #R_Score check_r(a[1],2)
        a[1] -= 1
    elif((x=='C' or x=='c') and turn%2==0):
        arr[a[2]][2*2]='Y'
        turn += 1
        #Y_Score check_y(a[2],4)
        a[2] -= 1
    elif((x=='C' or x=='c') and turn%2==1):
        arr[a[2]][2*2]='R'
        turn += 1
        #R_Score check_r(a[2],4)
        a[2] -= 1
    elif((x=='D' or x=='d') and turn%2==0):
        arr[a[3]][2*3]='Y'
        turn += 1
        #Y_Score check_y(a[3],6)
        a[3] -= 1
    elif((x=='D' or x=='d') and turn%2==1):
        arr[a[3]][2*3]='R'
        turn += 1
        #R_Score check_r(a[3],6)
        a[3] -= 1
    elif((x=='E' or x=='e') and turn%2==0):
        arr[a[4]][2*4]='Y'
        turn += 1
        #Y_Score check_y(a[4],8)
        a[4] -= 1
    elif((x=='E' or x=='e') and turn%2==1):
        arr[a[4]][2*4]='R'
        turn += 1
        #R_Score check_r(a[4],8)
        a[4] -= 1
    elif((x=='F' or x=='f') and turn%2==0):
        arr[a[5]][2*5]='Y'
        turn += 1
        
        #Y_Score check_y(a[5],10)
        a[5] -= 1
    elif((x=='F' or x=='f') and turn%2==1):
        arr[a[5]][2*5]='R'
        turn += 1
        #R_Score check_r(a[5],10)
        a[5] -= 1

    elif((x=='G' or x=='g') and turn%2==0):
        arr[a[6]][2*6]='Y'
        turn += 1
        #Y_Score check_y(a[6],12)
        a[6] -= 1
    elif((x=='G' or x=='g') and turn%2==1):
        arr[a[6]][2*6]='R'
        turn += 1
        #R_Score check_r(a[6],12)
        a[6] -= 1
    
    t-=1

