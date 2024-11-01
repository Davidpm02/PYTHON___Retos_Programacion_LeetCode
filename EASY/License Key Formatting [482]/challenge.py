"""
DESCRIPTION:

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

  Input: s = "5F3Z-2e-9-w", k = 4
  Output: "5F3Z-2E9W"
  Explanation: The string s has been split into two parts, each part has 4 characters.
  Note that the two extra dashes are not needed and can be removed.

Example 2:

  Input: s = "2-5g-3-J", k = 2
  Output: "2-5G-3J"
  Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

 

Constraints:

    1 <= s.length <= 105
    s consists of English letters, digits, and dashes '-'.
    1 <= k <= 104


"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        """
        Summary:
            Método de la clase Solution encargado de formatear una
            cadena de texto que representa la clave de una licencia.

            El formateo de la cadena 's' se lleva a cabo teniendo en 
            cuenta el parámetro 'k'.
        Args:
            s (str) -- Clave de licencia que se desea formatear.
            k (int) -- Valor máximo de valores por grupo.
        Returns:
            str
        """

        # Lista de grupos por defecto en 's'.
        groups_in_s_array = s.split('-')

        # Lista con los caracteres de todos los grupos menos el inicial.
        last_chars_in_s_array = []
        for group in groups_in_s_array[1:]:
            for char in group:
                last_chars_in_s_array.append(char)

        # Lista de grupos que conforman la clave formateada.
        formated_license_key_array = [groups_in_s_array[0]]
        while True:
            if len(last_chars_in_s_array) == 0:
                break
            try:    
                group = last_chars_in_s_array[:k]
                formated_license_key_array.append("".join(group))
                del last_chars_in_s_array[:k]
            except IndexError:
                formated_license_key_array.append("".join(last_chars_in_s_array))
                break

        formated_license = "-".join(formated_license_key_array).upper()
        return formated_license
        