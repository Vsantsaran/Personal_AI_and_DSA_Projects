#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TicTacToe:
    def __init__(self):
        '''Constructor: X is AI and O is human'''
        self.p_X = 1
        self.p_O = -1
        self.psi = 5
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = self.p_O
        self.counter = 0

    def __call__(self, x, y):
        '''when we say game(x, y) then this method should be called. It'll return the board after making the move.'''
        # the difference between this function and result function is that this function actually makes changes to the board, whereas
        # the result function just shows how the board will look like had we chosen a particular coordinate.
        self.board[x][y] = self.current_player
        self.current_player = self.p_O if self.current_player != self.p_O else self.p_X
        return self.__str__()

    def __str__(self):
        '''return a proper representation of the board. It must contain only X's and O's.'''
        mapping = {1: 'X', -1: 'O', 0: ' '}
        temp = f'''{mapping[self.board[0][0]]} | {mapping[self.board[0][1]]} | {mapping[self.board[0][2]]}\n----------\n\
{mapping[self.board[1][0]]} | {mapping[self.board[1][1]]} | {mapping[self.board[1][2]]}\n----------\n\
{mapping[self.board[2][0]]} | {mapping[self.board[2][1]]} | {mapping[self.board[2][2]]}\n\n'''
        return temp

    def isOver(self):
        for row in self.board:  # Check rows
            if abs(sum(row)) == 3:
                return row[0]

        for col in zip(*self.board):  # Check columns
            if abs(sum(col)) == 3:
                return col[0]

        # Check diagonals
        if abs(self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3:
            return self.board[0][0]
        if abs(self.board[0][2] + self.board[1][1] + self.board[2][0]) == 3:
            return self.board[0][2]

        # Check for draw or ongoing game
        return 0 if all(all(cell != 0 for cell in row) for row in self.board) else self.psi

    def _isValid(self, x, y):
        '''this func (protected) will check whether the coordinates given by the player are valid or not. 
        Validity means - 1. whether there is already a number at that coordinate.
                        2. whether the coordinates are in the range - [0, 2], inclusive or not.
        '''
        return False if x < 0 or x > 2 or y < 0 or y > 2 or self.board[x][y] else True

    def __actions(self):
        '''this function returns the coordinates of all possible moves in a certain scenario'''
        moves = []
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    moves.append((i, j))
        return moves

    def findScore(self, is_over):
        if is_over == 1:
            return 10
        if is_over == -1:
            return -10
        if not is_over:
            return 0

    def maximizer(self, alpha, beta):
        self.counter += 1
        print(self.counter)

        is_over = self.isOver()
        if is_over != self.psi:
            return self.findScore(is_over), None

        best_score = float('-inf')
        best_move = None

        for move in self.__actions():
            i, j = move
            self.board[i][j] = self.p_X
            self.current_player = self.p_O
            score, _ = self.minimizer(alpha, beta)
            self.board[i][j] = 0
            self.current_player = self.p_X

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break

        return best_score, best_move

    def minimizer(self, alpha, beta):
        is_over = self.isOver()
        if is_over != self.psi:
            return self.findScore(is_over), None

        best_score = float('inf')
        best_move = None

        for move in self.__actions():
            i, j = move
            self.board[i][j] = self.p_O
            self.current_player = self.p_X
            score, _ = self.maximizer(alpha, beta)
            self.board[i][j] = 0
            self.current_player = self.p_O

            if score < best_score:
                best_score = score
                best_move = move

            beta = min(beta, best_score)
            if beta <= alpha:
                break

        return best_score, best_move

    def makeMove(self):
        '''AI decides the best move using minimax'''
        alpha = float('-inf')
        beta = float('inf')
        _, best_move = self.maximizer(alpha, beta)
        if best_move:
            print(self(best_move[0], best_move[1]))

def play(game):
    print(game)
    while True:
        is_over = game.isOver()
        if is_over == 1:
            print('Winner: AI.')
            break
        elif is_over == -1:
            print('Winner: Human.')
            break
        elif is_over == 0:
            print("Draw!!!")
            break

        move = input("Enter your move [row col]: ")
        # print(type(move), move)
        x, y = [int(i) for i in move.split()]
        if not game._isValid(x, y):
            print("Move's not valid.")
            continue
        print(game(x, y))
        if game.isOver() == game.psi:
            print("AI is processing the move...")
            game.makeMove()
            game.counter = 0

if __name__ == '__main__':
    game = TicTacToe()
    play(game)


# In[ ]:




