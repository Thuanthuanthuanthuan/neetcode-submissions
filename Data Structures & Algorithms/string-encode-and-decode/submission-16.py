class Solution:

    def encode(self, strs: List[str]) -> str:

        # length + delimiter + s
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res



    def decode(self, s: str) -> List[str]:

        # length + delimiter + s
        res = []
        i = 0

        # find delimiter
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # find length of s
            length = int(s[i : j])

            # append string
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res
