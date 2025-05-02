"""
DESCRIPTION:

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.

"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        """
        Determina el estado final de los dominós después de que todas
        las fuerzas se hayan aplicado.
        
        params:
            dominoes: Una cadena que representa el estado inicial de los dominós.
                      'L' indica un dominó empujado hacia la izquierda.
                      'R' indica un dominó empujado hacia la derecha.
                      '.' indica un dominó vertical sin empujar.
        
        returns:
            str
        """

        n = len(dominoes)
        # Creamos un array para almacenar las fuerzas netas
        # Positivo significa fuerza hacia la derecha, negativo hacia la izquierda
        fuerza = [0] * n
        
        # Procesamos las fuerzas de izquierda a derecha
        fuerza_acumulada = 0
        for i in range(n):
            if dominoes[i] == 'R':
                # Fuerza máxima hacia la derecha
                fuerza_acumulada = n
            elif dominoes[i] == 'L':
                # No hay fuerza hacia la derecha
                fuerza_acumulada = 0
            else:
                # La fuerza disminuye con la distancia
                fuerza_acumulada = max(fuerza_acumulada - 1, 0)
            
            fuerza[i] += fuerza_acumulada
        
        # Procesamos las fuerzas de derecha a izquierda
        fuerza_acumulada = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                # Fuerza máxima hacia la izquierda
                fuerza_acumulada = n
            elif dominoes[i] == 'R':
                # No hay fuerza hacia la izquierda
                fuerza_acumulada = 0
            else:
                # La fuerza disminuye con la distancia
                fuerza_acumulada = max(fuerza_acumulada - 1, 0)
            
            # Restamos la fuerza hacia la izquierda para obtener la fuerza neta
            fuerza[i] -= fuerza_acumulada
        
        # Convertimos las fuerzas netas en el estado final de los dominós
        resultado = []
        for f in fuerza:
            if f > 0:
                resultado.append('R')
            elif f < 0:
                resultado.append('L')
            else:
                resultado.append('.')
        
        return ''.join(resultado)