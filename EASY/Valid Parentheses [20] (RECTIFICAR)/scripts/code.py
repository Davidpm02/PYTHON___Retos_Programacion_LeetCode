"""
DESCRIPTION:

## TODO => Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

  Input: s = "()"
  Output: true


Example 2:

  Input: s = "()[]{}"
  Output: true


Example 3:

  Input: s = "(]"
  Output: false
 

## Constraints:

  1 <= s.length <= 104
  s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
          Determines if a given string of parentheses is valid.

          Args:
              s (str): A string of parentheses, '(', ')', '{', '}', '[', ']'.

          Returns:
              bool: True if the string is valid, False otherwise.
        """
        
        # Defino un diccionario que mapee el número de apariciones de cada caracter de inicio y fin
        possible_signs_dict_counter = {
          "(":0,
          ")":0,
          "[":0,
          "]":0,
          "{":0,
          "}":0,
        }
        
        index_possible_signs_dict = {value:key for value, key in zip([0, 1, 2, 3, 4, 5, 6], ["(", ")", "[", "]", "{", "}"])}
        
        # Defino un nuevo diccionario que mapee cada tipo de paréntesis con un valor boleano
        checking_bool_parentheses_dict = {
          "()":True,
          "[]":True,
          r"{}":True
        }
        
        # Itero sobre el contenido del parámetro "s":
        for char in s:
          if char in possible_signs_dict_counter:
            possible_signs_dict_counter[char] += 1
            
        # Reviso el contenido del diccionario de apariciones
        for index, (key, value) in enumerate(possible_signs_dict_counter.items()):
          
         
          if (index%2 == 0):
            try:
              actual_key = key
              next_key = index_possible_signs_dict[index + 1]
              print(actual_key, next_key)
              if possible_signs_dict_counter[actual_key] == possible_signs_dict_counter[next_key]:
                continue
              elif possible_signs_dict_counter[actual_key] != possible_signs_dict_counter[next_key]:
                print("Entro aqui, index ==>", index)
                if index == 0:
                  checking_bool_parentheses_dict["()"] = False
                elif index == 2:
                  checking_bool_parentheses_dict["[]"] = False
                elif index == 4:
                  checking_bool_parentheses_dict[r"{}"] = False
            except KeyError:
              break
            

        print(possible_signs_dict_counter)
        print(checking_bool_parentheses_dict)  
        # Retorno un resultado
        if False in checking_bool_parentheses_dict.values():
          return False
        else:
          return True
        
        
if __name__ == "__main__":
  
  s = r"()[]{}"
  solution = Solution()
  sol = solution.isValid(s=s)
  print(sol)
        