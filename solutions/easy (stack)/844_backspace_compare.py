class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        for c in s:
            if c == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        stackT = []
        for c in t:
            if c == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)
 
        return stackS == stackT