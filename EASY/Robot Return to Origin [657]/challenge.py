"""
DESCRIPTION:

There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

Example 1:

  Input: moves = "UD"
  Output: true
  Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:

  Input: moves = "LL"
  Output: false
  Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

 

Constraints:

    1 <= moves.length <= 2 * 104
    moves only contains the characters 'U', 'D', 'L' and 'R'.

"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        """
        Analiza los movimientos realizados por un robot y verifica
        si el robot a vuelto a su posición de origen al finalizar.

        La función retorna True si el robot ha vuelto a su posición
        de origen, y False en caso constrario.

        params:
            moves (str)
        
        returns:
            bool
        """

        # Defino una variable que almacene las coordenadas de posición
        coords = [0, 0]

        # Convierto 'moves' en una array
        moves_array = [move for move in moves]

        # Actualizado la posición del robot tras cada movimiento
        for move in moves_array:
            if (move == 'U'):
                coords[1] +=1
            elif (move == 'D'):
                coords[1] -=1
            elif (move == 'L'):
                coords[0] -=1
            elif (move == 'R'):
                coords[0] +=1
        
        # Reviso el estado final de la posición del robot
        return True if ((coords[0] == 0) and (coords[1] == 0)) else False