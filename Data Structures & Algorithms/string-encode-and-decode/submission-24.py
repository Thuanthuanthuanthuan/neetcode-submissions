class Solution:

    def encode(self, strs: List[str]) -> str:

        # code: length + # + s
        res = []
        
        for s in strs:
            length = str(len(s))
            res.append(length + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        #code: length + # + s

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res


