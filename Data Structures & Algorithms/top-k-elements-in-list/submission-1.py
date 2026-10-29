class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for n in nums:
            my_dict[n] = my_dict.get(n,0) + 1

        my_list = list(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        keys = [pair[0] for pair in my_list]
        return keys[:k]