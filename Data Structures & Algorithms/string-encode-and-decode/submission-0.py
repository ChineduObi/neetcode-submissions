class Solution:

    def encode(self, strs: List[str]) -> str:
        red = ""
        for s in strs:
            red += str(len(s)) + "#" + s
        return red

    def decode(self, s: str) -> List[str]:
        red, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            red.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return red
