import ctypes

import ctypes

class HammingWeight:
    def hammingWeight(self, n:int):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n, cnt = n & (n-1), cnt + 1
        return cnt

def test_hamming_weight():
    ts = HammingWeight()
    answer = ts.hammingWeight(15)
    assert answer == 4

if __name__ == "__main__":
    test_hamming_weight()

