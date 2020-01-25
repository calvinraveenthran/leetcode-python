import functools

class SubtractProdSum:
    def add(self, x:str,y:str)-> int: return int(x)+int(y)
    def product(self, x:str,y:str) -> int: return int(x)*int(y)
    def subtractProductAndSum(self, n: int) -> int:
        if n < 10: 
            return 0
        return functools.reduce(self.product, str(n)) - functools.reduce(self.add, str(n))

