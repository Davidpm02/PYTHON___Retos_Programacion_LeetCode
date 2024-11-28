"""
DESCRIPTION:

Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

 

A single number is a number that appeared only once in the MyNumbers table.
Find the largest single number. If there is no single number, report null.
The result format is in the following example.

 

Example 1:

Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+

Output: 
+-----+
| num |
+-----+
| 6   |
+-----+

Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.



Example 2:

Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+

Output: 
+------+
| num  |
+------+
| null |
+------+

Explanation: There are no single numbers in the input table so we return null.

"""

import pandas as pd
from collections import Counter

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:

    """
    Encuentra el número con una única aparición dentro del 'my_numbers'
    y lo retorna dentro de un nuevo objeto DataFrame.

    En caso de que no existan números con una única aparición, la función
    retorna un DataFrame con un único registro nulo.

    params:
        my_numbers (pd.DataFrame)
    
    returns:
        pd.DataFrame
    """

    numbers_record = list(my_numbers['num'].values)
    counter_of_numbers = Counter(numbers_record)

    single_number_list = []
    for key, value in counter_of_numbers.items():
        
        # Cada elemento de Counter tiene la estructura (key:value) --> Diccionario
        if (value == 1):
            single_number_list.append(key)
        else:
            continue
    
    if (len(single_number_list) > 0):
        highest_single_number = max(single_number_list)
    else:
        highest_single_number = None
    return pd.DataFrame(data=[highest_single_number],
                        columns=['num'])