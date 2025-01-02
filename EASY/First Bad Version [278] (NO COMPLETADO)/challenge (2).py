"""
DESCRIPTION:

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

  Input: n = 5, bad = 4
  Output: 4
  Explanation:
   call isBadVersion(3) -> false
   call isBadVersion(5) -> true
   call isBadVersion(4) -> true
   Then 4 is the first bad version.

Example 2:

  Input: n = 1, bad = 1
  Output: 1

 

Constraints:

    1 <= bad <= n <= 231 - 1

"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        """
        """

        versions_array = [_ for _ in range(1, n + 1)]
        index_middle_version_in_n = ((len(versions_array)) // 2)
        middle_value = versions_array[index_middle_version_in_n]
        at_least_one_bad = False
        is_false_again = False

        if n < 1000:
            for v in versions_array:
                print(f"isBadVersion({v}) ===> {isBadVersion(v)}")
                if isBadVersion(v) == True:
                    return v

        while True:

            if len(versions_array) == 1:
                return versions_array[-1]
            print('Array actual:', versions_array)
            print('Indice a examinar:', index_middle_version_in_n)
            print('Version correspondiente al indice a examinar:', middle_value)
            if isBadVersion(versions_array[versions_array.index(middle_value)]) == True:
                print(f'La version {middle_value} es mala.')
                if len(versions_array) == 2:
                    return middle_value
                at_least_one_bad = True
                index_middle_version_in_n = ((len(versions_array[:index_middle_version_in_n])) // 2)
                middle_value = versions_array[index_middle_version_in_n]
                versions_array = versions_array[:versions_array.index(middle_value)]
                continue
            else:
                print(f'La version {versions_array[index_middle_version_in_n]} es buena.')
                if len(versions_array) == 2:
                    try:
                        return versions_array[index_middle_version_in_n + 1]
                    except:
                        return versions_array[index_middle_version_in_n - 1]
                index_middle_version_in_n = ((len(versions_array[index_middle_version_in_n + 1:])) // 2)
                middle_value = versions_array[index_middle_version_in_n]
                versions_array = versions_array[versions_array.index(middle_value):]
                if at_least_one_bad == True:
                    break
                continue
        return versions_array[-1]