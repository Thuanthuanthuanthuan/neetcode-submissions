class Solution:

    def encode(self, strs: List[str]) -> str:

        # length + # + s
        res = ""

        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        # length + # + s
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i : j])

            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res

           


