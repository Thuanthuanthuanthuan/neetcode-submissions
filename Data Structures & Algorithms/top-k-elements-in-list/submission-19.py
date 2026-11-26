class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        count = {}

        #count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        #group them
        for num, cnt in count.items():
            buckets[cnt].append(num)

        #ans list
        ansList = []
        #retrieve
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ansList.append(num)

                if len(ansList) == k:
                    return ansList

        