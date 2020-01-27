class SplitAString:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        list_s = list(s)
        for i in list_s:
            if i == "R":
                count = count + 1
            elif i =="L":
                count = count - 1
            if count == 0:
                res = res + 1
        return res