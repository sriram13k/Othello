import math
from copy import deepcopy

class Player():

    def __init__(self,depth,color):
        self.bind_flag = False
        self.color = color                      # -1 for black, 1 for white
        self.depth = depth
        self.nodes_expanded = 0

    def bind(self,game):
        self.game = game
        self.bind_flag = True

    def move(self):
        #optimal_move, _ =  self.minimax_search()
        optimal_move, _ = self.alpha_beta_search()
        print(self.nodes_expanded)
        self.nodes_expanded = 0
        return optimal_move

    def minimax_search(self):
        if not self.bind_flag:
            print("Error , player hasn't been binded")

        (move,value) = self.minimax_search_helper(self.game.board,self.depth,True)
        return (move,value)

    def simple_heuristic(self,board):
        white_score = 0
        black_score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    white_score += 1
                elif board[i][j] == -1:
                    black_score += 1
        if self.color == 1:
            return white_score - black_score
        else:
            return black_score - white_score

    def static_heuristic(self,board):                   # V. Sannidhanam and M. Annamalai, “Ananalysis of heuristics in othello,” 2015
        static_weights =    [   [4,-3,2,2,2,2,-3,4],
                                [-3,-4,-1,-1,-1,-1,-4,-3],
                                [2,-1,1,0,0,1,-1,2],
                                [2,-1,0,1,1,0,-1,2],
                                [2,-1,0,1,1,0,-1,2],
                                [2,-1,1,0,0,1,-1,2],
                                [-3,-4,-1,-1,-1,-1,-4,-3],
                                [4,-3,2,2,2,2,-3,4]
                            ]
        white_score = 0
        black_score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    white_score += static_weights[i][j]
                elif board[i][j] == -1:
                    black_score += static_weights[i][j]
        if self.color == 1:
            return white_score - black_score
        else:
            return black_score - white_score

    def dynamic_heuristic(self,board):
        score = 0
        cornerVal = 25
        adjacentVal = 5
        sideVal = 5
        for x in range(8):
            for y in range(8):
                if board[x][y] == 0:
                    continue
                add = 1
                if (x==0 and y==1) or (x==1 and 0<=y<=1):
                    if board[0][0]==self.color:
                        add = sideVal
                    else:
                        add = -adjacentVal
                elif (x==0 and y==6) or (x==1 and 6<=y<=7):
                    if board[7][0]==self.color:
                        add = sideVal
                    else:
                        add = -adjacentVal
                elif (x==7 and y==1) or (x==6 and 0<=y<=1):
                    if board[0][7]==self.color:
                        add = sideVal
                    else:
                        add = -adjacentVal
                elif (x==7 and y==6) or (x==6 and 6<=y<=7):
                    if board[7][7]==self.color:
                        add = sideVal
                    else:
                        add = -adjacentVal
                elif (x==0 and 1<y<6) or (x==7 and 1<y<6) or (y==0 and 1<x<6) or (y==7 and 1<x<6):  #Edge tiles worth 5 
                    add=sideVal
                elif (x==0 and y==0) or (x==0 and y==7) or (x==7 and y==0) or (x==7 and y==7):      #Corner tiles worth 15
                    add = cornerVal
                if board[x][y]==self.color:
                    score+=add
                elif board[x][y]==-self.color:
                    score-=add
	    
        return score

    def minimax_search_helper(self,current_board,depth,is_player):
        self.nodes_expanded += 1
        board = deepcopy(current_board)
        if depth == 0:
           #return ((-1,-1),self.simple_heuristic(board))
           #return ((-1,-1),self.static_heuristic(board))
           return ((-1,-1),self.dynamic_heuristic(board))
        
        if is_player:
            optimal_value = -math.inf
            optimal_move = (-4,-4)
            moves = self.game.get_valid_moves(board)
            for move in moves:
                x, y = move
                new_board = self.game.move(board,self.color,x,y)
                _ , value = self.minimax_search_helper(new_board,depth-1,False)
                #print("Value" + str(value))
                if value > optimal_value:
                    optimal_value = value
                    optimal_move = move
                    
            return (optimal_move,optimal_value)
        
        else:
            optimal_value = math.inf
            optimal_move = (-1,-1)
            value = math.inf
            moves = self.game.get_valid_moves(board)
            for move in moves:
                x, y = move
                new_board = self.game.move(board,-self.color,x,y)
                _ , value = self.minimax_search_helper(new_board,depth-1,True)
                if value < optimal_value:
                    optimal_value = value
                    optimal_move = move
                    
            return (optimal_move,optimal_value)
        
    def alpha_beta_search(self):
        if not self.bind_flag:
            print("Error , player hasn't been binded")

        (move,value) = self.alpha_beta_search_helper(self.game.board,self.depth,-math.inf, math.inf, True)
        return (move,value)

    
    def alpha_beta_search_helper(self,current_board,depth,alpha,beta,is_player):
        self.nodes_expanded += 1 
        board = deepcopy(current_board)
        if depth == 0:
           #return ((-1,-1),self.simple_heuristic(board))
           #return ((-1,-1),self.static_heuristic(board))
           return ((-1,-1),self.dynamic_heuristic(board))
        
        if is_player:
            optimal_value = -math.inf
            optimal_move = (-4,-4)
            moves = self.game.get_valid_moves(board)
            for move in moves:
                x, y = move
                new_board = self.game.move(board,self.color,x,y)
                _ , value = self.alpha_beta_search_helper(new_board,depth-1,alpha,beta,False)
                #print("value" + str(value))
                if value > optimal_value:
                    optimal_value = value
                    optimal_move = move
                alpha = max(alpha,optimal_value)
                if alpha >= beta:
                    break
            return (optimal_move,optimal_value)
        
        else:
            optimal_value = math.inf
            optimal_move = (-1,-1)
            value = math.inf
            moves = self.game.get_valid_moves(board)
            for move in moves:
                x, y = move
                new_board = self.game.move(board,-self.color,x,y)
                _ , value = self.alpha_beta_search_helper(new_board,depth-1,alpha,beta,True)
                if value < optimal_value:
                    optimal_value = value
                    optimal_move = move
                beta = min(beta,optimal_value)
                if alpha >= beta:
                    break
                    
            return (optimal_move,optimal_value)
        