"""
DESCRIPTION:

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.

"""

from typing import List, Tuple
from collections import deque

class Solution:
    def _label_to_coords(self, label: int, n: int) -> Tuple[int, int]:
        """
        Dado un label (1-indexed) de casilla y el tamaño n del tablero,
        calculo las coordenadas (fila, columna) en la matriz.

        params:
            label (int)
            n (int)

        returns:
            Tuple[int, int]

        """

        lbl0 = label - 1
        row_from_bottom = lbl0 // n
        r = n - 1 - row_from_bottom
        col_in_row = lbl0 % n

        if row_from_bottom % 2 == 0:
            c = col_in_row
        else:
            c = n - 1 - col_in_row

        return (r, c)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Calcula el número mínimo de lanzamientos de dado para llegar
        desde la casilla 1 hasta la casilla n^2 en un tablero de
        serpientes y escaleras dado en formato Boustrophedon.

        params:
            board (List[List[int]])
        
        returns:
            int

        """
        
        n = len(board)
        n2 = n * n

        queue = deque()
        queue.append((1, 0))  # Empiezo en casilla 1 con 0 movimientos
        visited = set([1])    # Marco la casilla 1 como visitada

        while queue:
            curr_label, moves = queue.popleft()
            if curr_label == n2:
                return moves

            for dice in range(1, 7):
                next_label = curr_label + dice
                if next_label > n2:
                    break

                r, c = self._label_to_coords(next_label, n)
                if board[r][c] != -1:
                    destination = board[r][c]
                else:
                    destination = next_label

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

        return -1