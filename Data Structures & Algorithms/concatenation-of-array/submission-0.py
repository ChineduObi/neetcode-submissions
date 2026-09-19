#This is just a duplication of the array. Create an array with length 2n of the original array and for Loop the length of the array and add simultaneously add the number at both indices (i and i + n).
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2*n

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans