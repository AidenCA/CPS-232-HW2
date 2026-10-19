# CPS-232-HW2

**Task Description**

This assignment focuses on designing two exact search algorithms and explaining their correctness and time complexity. The first problem asks whether a target number belongs to a set of natural numbers, with a required search time of O(log n) or better. The second problem asks for an efficient way to find a small target in an ascending list. Both solutions must explain why they always produce the correct result and how their running times are calculated.

**Code Description**

My code is written in Python and uses binary search and exponential search.

For Problem 1, I sort the numbers once and then use binary search to check whether the target is present. Binary search checks the middle element and eliminates half of the remaining search range each time. Sorting takes O(n log n), while each search afterward takes O(log n). This solution assumes preprocessing is allowed.

For Problem 2, I use exponential search to check positions 1, 2, 4, 8, and so on until I find a range that could contain the target. I then use binary search within that range. This takes O(log(p + 2)), where p is the target’s position or insertion position. It is especially useful for targets near the beginning, although its worst-case time is still O(log n).

The code includes comments explaining each step and examples showing successful and unsuccessful searches. Binary search returns an index or -1 when the target is absent, while the membership function for Problem 1 returns True or False.
