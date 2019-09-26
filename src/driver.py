import othello

def main():
    
    root = othello.tk.Tk()
    game = othello.Othello(1,1,master= root)
    game.mainloop()

           

if __name__ == "__main__":
    main()

