class BasePiece:

    @staticmethod
    def __popcount0(mask):
        count = 0
        while (mask > 0):
            if mask & 1 > 0:
                count += 1
            mask >>= 1

        return count


    @staticmethod
    def __popcount1(mask):
        count = 0
        while (mask > 0):
            count += 1
            mask &= mask - 1

        return count

    @staticmethod
    def popcount(mask, mode:int = 0):
        if mode == 1: return BasePiece.__popcount1(mask)
        return BasePiece.__popcount0(mask)

    @staticmethod
    def normalizeMask(mask):
        return mask & 0xffffffffffffffff

    def getMoves(self, position:int):
        pass

    

