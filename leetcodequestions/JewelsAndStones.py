class JewelsAndStones:
    def numJewelsInStones(self, J: str, S: str) -> int:
        list_j = list(J)
        list_s = list(S)
        return len([x for x in list_s if x in list_j])