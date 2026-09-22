'''The optimized solution uses a hashmap to store the value and index and as we iterate through the array we find the difference and compare them'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            seen[n] = i

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]

        return []