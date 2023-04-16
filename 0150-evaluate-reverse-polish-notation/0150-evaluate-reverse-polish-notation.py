class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                s.append(int(i))
            else:
                y = s.pop()
                x = s.pop()
                if i == "+":
                    z = x+y
                    s.append(z)
                elif i == "-":
                    z = x-y
                    s.append(z)
                elif i == "*":
                    z = x*y
                    s.append(z)
                else:
                    s.append(int(x/y))
        ret = s[0]
        return ret
        