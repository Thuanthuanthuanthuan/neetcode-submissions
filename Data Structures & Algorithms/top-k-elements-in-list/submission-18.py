class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        seen = {}

        # get count
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        #add to buckets
        for num, cnt in seen.items():
            buckets[cnt].append(num)


        answerList = []

        #retrieve from buckets
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answerList.append(num)
                if len(answerList) == k:
                    return answerList
        
        


        