import ctypes

class SumOftwoIntegers:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
             """
        A =  ctypes.c_int32(a)
        B =  ctypes.c_int32(b)
        result = A.value^B.value
        carry  = (A.value&B.value) <<1 
        if carry:
            return self.getSum(result, carry)
        else:
            return result

def test_get_sum():
    ts = SumOftwoIntegers()
    answer = ts.getSum(5, 6)
    assert answer == 11
    answer = ts.getSum(5, -6)
    assert answer == -1
    answer = ts.getSum(-1, 1)
    assert answer == 0


if __name__ == "__main__":
    test_get_sum()

