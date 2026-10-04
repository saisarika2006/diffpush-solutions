# Largest element in array — 01-arrays
# For full question visit: https://diffpush.pages.dev/solve/largest-element-in-array
# Solved via DiffPush — pushed from the workspace on green.
class Solution:
    def largestElement(self, arr: list[int], n: int) -> int:
        largest = arr[0]

        for i in range(1, n):
            if arr[i] > largest:
                largest = arr[i]

        return largest
# Passed test cases:
# 1. Input: {"A": [1, 8, 7, 56, 90], "n": 5} => Expected: 90
# 2. Input: {"A": [4, 15, 8, 23, 16, 42], "n": 6} => Expected: 42
# 3. Input: {"A": [-7], "n": 1} => Expected: -7
