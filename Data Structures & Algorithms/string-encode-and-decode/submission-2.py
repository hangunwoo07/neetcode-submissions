class Solution:

    def encode(self, strs: List[str]) -> str:
        res_string = ""
        for string in strs:
            res_string = f"#{len(string)}#".join([res_string, string])
        
        return res_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # s[i] should be '#'
            j = i + 1

            # Find the second '#'
            while s[j] != "#":
                j += 1

            string_len = int(s[i + 1:j])

            start = j + 1
            end = start + string_len

            res.append(s[start:end])

            i = end

        return res