import player
import tkinter as tk


class Othello(tk.Frame):
    def __init__ (self,player1, player2,master = None):
        super().__init__(master)
        self.player1 = player1
        self.player2 = player2
        self.master = master
        self.screen = tk.Canvas(self.master, width=600, height=600)
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.turn = -1                                                      # -1 for black, 1 for white
        self.valid_moves_indicators = []  
        self.create_board()
        self.play()


    def create_board(self):
        self.board[3][3] =  1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] =  1
        
        for i in range(8):
            for j in range(8):
                if((i+j) % 2 == 0):
                    self.screen.create_rectangle(i*75, j*75, (i+1)*75, (j+1)*75, fill="darkgreen")
                else:
                    self.screen.create_rectangle(i*75, j*75, (i+1)*75, (j+1)*75, fill="SpringGreen3")

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    self.screen.create_oval(i*75+ 7.5, j*75+ 7.5,i*75 +67.5,j*75 + 67.5, fill = "white" , outline = "white")
                elif self.board[i][j] == -1:
                    self.screen.create_oval(i*75+ 7.5, j*75 +7.5,i*75+ 67.5,j*75 + 67.5, fill = "black" , outline = "black")
        self.screen.pack()
        
        return
        
    def update_board(self):
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    self.screen.create_oval(i*75+ 7.5, j*75+ 7.5,i*75 +67.5,j*75 + 67.5, fill = "white" , outline = "white")
                elif self.board[i][j] == -1:
                    self.screen.create_oval(i*75+ 7.5, j*75 +7.5,i*75+ 67.5,j*75 + 67.5, fill = "black" , outline = "black")

        for valid_move_indicator in self.valid_moves_indicators:
            self.screen.delete(valid_move_indicator)
        
        valid_moves = self.get_valid_moves()
        for i,j in valid_moves:
            self.valid_moves_indicators.append(self.screen.create_oval(i*75+ 25, j*75+ 25,i*75 +50,j*75 + 50, fill = "orange" , outline = "orange"))
        
        return

        
    def is_valid_move(self,x,y):
        if not self.is_valid_posistion(x,y):
            return False

        if self.board[x][y] != 0:
            return False
        
        for (i,j) in [(1,1),(1,-1),(-1,1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
            current_x=x
            current_y=y
            if self.is_valid_posistion(x+i,y+j) and self.board[x+i][y+j] == -self.turn:
                while True:
                    current_x += i
                    current_y += j
                    
                    if not self.is_valid_posistion(current_x,current_y):
                        break
                    elif self.board[current_x][current_y] == -self.turn:
                        continue
                    elif self.board[current_x][current_y] == self.turn:
                        return True
                    elif self.board[current_x][current_y] == 0:
                        break
        
        return False
                
    
    def move(self,x,y):
        self.board[x][y] = self.turn
        for (i,j) in [(1,1),(1,-1),(-1,1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
            current_x=x
            current_y=y
            flips = []
            if self.is_valid_posistion(x+i,y+j) and self.board[x+i][y+j] == -self.turn:
                flag = False
                while True:
                    current_x += i
                    current_y += j
                    
                    if not self.is_valid_posistion(current_x,current_y):
                        print("Error, Invalid Move")
                    elif self.board[current_x][current_y] == -self.turn:
                        flips.append((current_x,current_y))
                        continue
                    elif self.board[current_x][current_y] == self.turn:
                        flag = True
                        break
                    elif self.board[current_x][current_y] == 0:
                        break
                
                if flag == True:
                    break
        
        

        for (x,y) in flips:
            print(x,y)
            self.board[x][y] = -self.board[x][y]
        
        self.turn = -self.turn
        self.update_board()
        return
        
    def get_valid_moves(self):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(i,j):
                    valid_moves.append((i,j))

        return valid_moves    
    
    def is_valid_posistion(self,x,y):
        if x>=0 and x<8:
            if y>=0 and y<8:
                return True
        
        return False
    
    def play(self):
        
        print(self.get_valid_moves())
        x = int(input("Enter x"))
        y = int(input("Enter y"))
        if(self.is_valid_move(x,y)):
            self.move(x,y)
        else:
            print("Enter Valid Move")
        self.master.after(1000,self.play)
    


        
            

