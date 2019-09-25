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
        self.create_board()
        self.turn = -1                                                  # -1 for black, 1 for white
        

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
        
    def update_board(self,x,y):
        self.board[x][y] = self.turn
        self.turn = -self.turn
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    self.screen.create_oval(i*75+ 7.5, j*75+ 7.5,i*75 +67.5,j*75 + 67.5, fill = "white" , outline = "white")
                elif self.board[i][j] == -1:
                    self.screen.create_oval(i*75+ 7.5, j*75 +7.5,i*75+ 67.5,j*75 + 67.5, fill = "black" , outline = "black")

        self.screen.pack()


def main():
    root = tk.Tk()
    game = Othello(1,1,master= root) 
    game.mainloop()

           

if __name__ == "__main__":
    main()