class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            seen[num] = seen.get(num,0) + 1

        for num, cnt in seen.items():
            freq[cnt].append(num)

        answerList = []
        for i in range(len(freq) -1 , 0, -1):
            for num in freq[i]:
                answerList.append(num)
                if len(answerList) == k:
                    return answerList
        