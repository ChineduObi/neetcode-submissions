class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"}": "{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c not in bracketMap: #Opening Bracket
                stack.append(c)
            else: #closing bracket
                if not stack: #No corresponding opening Bracket
                    return False

                opening = stack.pop()
                if opening != bracketMap[c]: 
                    return False   

        return not stack          


