class Game:
    def __init__(self):
        # Initialize the game state
        self.arr = [
            list("OOOOOOO"),
            list("OOOOOOO"),
            list("OOOOOOO"),
            list("OOOOOOO"),
            list("OOOOOOO"),
            list("OOOOOOO"),
        ]
        self.turn = 0  # 0 for Yellow, 1 for Red

    def make_move(self, col):
        # Find the lowest available row in the given column
        for row in reversed(range(6)):  # Start from the bottom row
            if self.arr[row][col] == "O":
                self.arr[row][col] = "Y" if self.turn == 0 else "R"
                self.turn = 1 - self.turn  # Switch turns
                print(f"Y Score is {self.check('Y')} \t and \t R Score is {self.check('R')} \n")
                return row, col  # Return the row and column of the move
        return None  # If the column is full, return None

    def get_token(self, row, col):
        # Get the token (Y or R) from the board at a given position
        return self.arr[row][col]

    def Row_check(self,x , color):
        cnt=0
        score=0
        for i in range(0,7):
            if(self.arr[x][i]== color and score == 0):
                cnt += 1
            elif(self.arr[x][i]== color and score != 0):
                cnt += 1
                score+=1
            elif(self.arr[x][i]!= color ):
                cnt=0
            elif(self.arr[x][i]!= color and score!=0):
                pass
                return score
            if(cnt==4):
                score+=1
        pass
        return score

    def col_check(self,x , color):
        cnt=0
        score=0
        for i in range(0,6,1):
            if(self.arr[i][x]== color and score == 0):
                cnt += 1
            elif(self.arr[i][x]== color and score != 0):
                cnt += 1
                score+=1
            elif(self.arr[i][x]!= color ):
                cnt=0
            elif(self.arr[i][x]!= color and score!=0):
                pass
                return score
            if(cnt==4):
                score+=1
        pass
        return score


    def all_row(self,color):
        score=0
        for i in range(0,6):
            score+=self.Row_check(i,color)
        pass
        return score

    def valid(self,x , y):
        if(x < 6 and y < 7 and x >= 0 and y >= 0):
            pass
            return True
        else:
            pass
            return False

    def diagonal_check(self,x, y, color):
        cnt=0
        score=0
        
        while(self.valid(x , y)):
            
            if(self.arr[x][y]==color and score == 0):
                cnt += 1
            elif(self.arr[x][y]==color and score != 0):
                cnt += 1
                score+=1
            elif(self.arr[x][y]!=color):
                cnt=0
            elif(self.arr[x][y]!=color and score!=0):
                pass
                return score
            if(cnt==4):
                score+=1
            x += 1
            y += 1
        pass
        return score

    def x_diagonal_check(self,x, y, color):
        cnt=0
        score=0
        
        while(self.valid(x , y)):
            if(self.arr[x][y]==color and score == 0):
                cnt += 1
            elif(self.arr[x][y]==color and score != 0):
                cnt += 1
                score+=1
            elif(self.arr[x][y]!=color):
                cnt=0
            elif(self.arr[x][y]!=color and score!=0):
                pass
                return score
            if(cnt==4):
                score+=1
            x += 1
            y -= 1
        pass
        return score

    def all_x(self,color):
        score = 0
        for i in range(4):
            score += self.diagonal_check(i, 0 ,color)
        for j in range(1,4): # todoooooooooooo
            score += self.diagonal_check(0, j ,color)
        for i in range(0,3):
            score += self.x_diagonal_check(i, 6 ,color)
        for j in range(3,6):
            score += self.x_diagonal_check(0, j ,color)

        pass
        return score


    def all_col(self,color):
        score=0
        for i in range(0,7):
            score+=self.col_check(i, color)
        pass
        return score

    def check(self,color):
        pass
        return self.all_col(color) + self.all_row(color) + self.all_x(color)


