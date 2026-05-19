class Solution:

    def encode(self, strs: List[str]) -> str:
        res_string = ""
        for string in strs:
            res_string = f"#{len(string)}#".join([res_string, string])
        
        return res_string

    def decode(self, s: str) -> List[str]:
        res_list: List[str] = []

        i = 0
        while i < len(s):
            if s[i] == "#":
                string_len = 0
                i += 1
                
                while s[i] != "#":
                    string_len *= 10
                    string_len += int(s[i])
                    i += 1
                
                string = ""
                for j in range(i+1, i+1+string_len):
                    string = "".join([string, s[j]])
                i = i + 1 + string_len

                res_list.append(string)
        
        return res_list
