#https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        """
        @param s: List of str of 1 <= len(s) <= 1000000
        TC: O(n)
        SC: O(1)
        Do not return anything, modify s in-place instead.
        """
        start_index = 0
        end_index = len(s) -1

        while start_index < end_index:
            Solution.swap_character(s, start_index, end_index)
            start_index += 1
            end_index -= 1


    @classmethod
    def swap_character(s, start, end):

        temp = s[end]

        s[end] = s[start]

        s[start] = temp

s = ["a", "b", "r", "a", "c", "a", "d", "a", "b", "r", "a"]
Solution.reverse_string(s)
print(s)
