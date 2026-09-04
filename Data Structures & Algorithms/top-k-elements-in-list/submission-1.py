class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num, cnt in count.items():
            buckets[cnt].append(num)

        answerList = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answerList.append(num)
                if len(answerList) == k:
                    return answerList