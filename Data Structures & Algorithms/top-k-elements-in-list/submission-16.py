class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    
        tracker = {} # track integer n its count
        buckets = [[] for i in range(len(nums) + 1)]

        # get the count
        for num in nums:
            tracker[num] = tracker.get(num,0) + 1

        # populate the buckets
        for num, cnt in tracker.items():
            buckets[cnt].append(num)

        # list for final output
        res = []

        
        # start at the last buckets
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        