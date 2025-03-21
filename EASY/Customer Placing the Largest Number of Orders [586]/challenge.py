"""
DESCRIPTION:

Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.

 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.
The result format is in the following example.

 

Example 1:

Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+


Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+


Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.

"""

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    """
    Encuentra el cliente con el mayor número de órdenes y retorna
    el identificador del cliente en un nuevo DataFrame.

    params:
        - orders (pd.DataFrame)
    
    returns:
        - pd.DataFrame
    """

    if (len(orders.index) == 0):
        return pd.DataFrame(data=[],
                            columns=['customer_number'])
                            
    orders_per_customer = orders['customer_number'].value_counts()
    customer_with_more_orders = orders_per_customer.index[0]

    return pd.DataFrame(data=[customer_with_more_orders],
                        columns=['customer_number'])