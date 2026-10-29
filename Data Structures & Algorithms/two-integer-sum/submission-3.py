class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            v = nums[i]
            other = target - v 
            if v in my_map.keys():
                result = []
                val1 = my_map[v]
                return [val1, i]
            my_map[other] = i
        return []
