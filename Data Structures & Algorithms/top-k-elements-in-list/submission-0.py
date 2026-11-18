class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        keys_list = list(counter.keys())
        sort_by_freq = sorted(keys_list, key=lambda key: counter[key], reverse=True)
        
        return sort_by_freq[0:k]
        
        