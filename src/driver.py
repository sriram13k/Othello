import othello
import player

def main():
    
    root = othello.tk.Tk()
    computer1 = player.Player(3,-1)
    computer2 = player.Player(4,1)
    game = othello.Othello(computer1,computer2,master= root)

    game.mainloop()

           

if __name__ == "__main__":
    main()

