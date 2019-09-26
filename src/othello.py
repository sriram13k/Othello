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
        self.white_score = 0
        self.black_score = 0
        self.turn = -1                                                      # -1 for black, 1 for white
        self.move_count = 0                                                 #Better name
        self.valid_moves = []
        self.valid_moves_indicators = []  
        self.screen.bind("<Button-1>", self.play)
        self.create_board()
        self.update_board()
        


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
        self.valid_moves = self.get_valid_moves()
        self.update_board()
        return
        
    def update_board(self):
        self.white_score = 0
        self.black_score = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    self.white_score += 1
                    self.screen.create_oval(i*75+ 7.5, j*75+ 7.5,i*75 +67.5,j*75 + 67.5, fill = "white" , outline = "white")
                elif self.board[i][j] == -1:
                    self.black_score += 1
                    self.screen.create_oval(i*75+ 7.5, j*75 +7.5,i*75+ 67.5,j*75 + 67.5, fill = "black" , outline = "black")


        

        for valid_move_indicator in self.valid_moves_indicators:
            self.screen.delete(valid_move_indicator)
        
        self.valid_moves_indicators = []
        
        for i,j in self.valid_moves:
            self.valid_moves_indicators.append(self.screen.create_oval(i*75+ 25, j*75+ 25,i*75 +50,j*75 + 50, fill = "orange" , outline = "orange"))
        
        return
    
#    def handle_click(self,event):
#        x = event.x //(75)
#        y = event.y //(75)
#        #print(x,y)
#        return (x,y)

        
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
        flips = []
        for (i,j) in [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]:
            current_x=x
            current_y=y
            if self.is_valid_posistion(x+i,y+j) and self.board[x+i][y+j] == -self.turn:
                flag = False
                aux_flips = []
                while True:
                    current_x += i
                    current_y += j
                    
                    if not self.is_valid_posistion(current_x,current_y):
                        break
                    elif self.board[current_x][current_y] == -self.turn:
                        aux_flips.append((current_x,current_y))
                        continue
                    elif self.board[current_x][current_y] == self.turn:
                        flag = True
                        break
                    elif self.board[current_x][current_y] == 0:
                        break
                
                if flag == True:
                    flips = flips + aux_flips
        
        #flips = set(flips)

        for (x,y) in flips:
            print(x,y)
            self.board[x][y] = -self.board[x][y]

        self.move_count += 1 
        self.turn = -self.turn
        self.valid_moves = self.get_valid_moves()
        self.update_board()
        
        if self.white_score == 0:
            print("Black Won")
            return -1
        elif self.black_score ==0:
            print("White Won")
            return 1
        
        if len(self.valid_moves) == 0:
            self.turn = -self.turn
            self.valid_moves = self.get_valid_moves()
            if(len(self.valid_moves) == 0):
                if self.white_score > self.black_score:
                    print("White Won")
                    return 1
                elif self.black_score > self.white_score:
                    print("Black Won")
                    return -1
                else:
                    print("Draw")
                    return 2
            
        return 0
        
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
    
    def play(self,event):
        self.update_board()

        x = event.x //(75)
        y = event.y //(75)
        print(x,y)
        if self.is_valid_move(x,y):
            self.move(x,y)
        else:
            return
