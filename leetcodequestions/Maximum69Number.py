class Maximum69Number:   
    def maximum69Number (self, num: int) -> int:
        length = len(str(num))
        
        for n in range(length):
            newNumStr = list(str(num))
            newNumStr[n] = "9"
            newNumStr= ''.join(newNumStr)
            newNum = int(newNumStr)
            if newNum > num:
                return newNum
        return num