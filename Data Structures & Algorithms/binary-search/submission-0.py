class Solution:
    def findMe(self, start: int, end: int, nums: List[int], target: int):
        if start > end:
            return -1
        
        middle = (start+end)//2

        if nums[middle] == target:
            return middle

        if nums[middle] < target:
            return self.findMe(middle+1, end, nums, target)

        if nums[middle] > target:
            return self.findMe(start, middle-1, nums , target)

    def search(self, nums: List[int], target: int) -> int:
        return self.findMe(0, len(nums)-1, nums, target)
        
    