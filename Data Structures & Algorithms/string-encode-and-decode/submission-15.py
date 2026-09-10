class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            # length + delimiter + s
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        #find delimiter
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            # get length of string
            length = int(s[i:j])

            #append to list
            res.append(s[j + 1: j + 1 + length])

            #move to next word
            i = j + 1 + length


        # return list
        return res
