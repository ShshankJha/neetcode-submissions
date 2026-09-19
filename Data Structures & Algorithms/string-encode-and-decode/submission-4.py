class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for item in strs:
            reversed_string = "".join(reversed(item))
            final += reversed_string + "`"
        
        return final



    def decode(self, s: str) -> List[str]:

        restore = s.split("`")
        fil = []
        for i in range(len(restore)-1):
            res_str = "".join(reversed(restore[i]))
            fil.append(res_str)
        
        return fil
