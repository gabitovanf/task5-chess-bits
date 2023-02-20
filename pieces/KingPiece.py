from BasePiece import BasePiece

class KingPiece(BasePiece):
    def getMoves(self, position:int):
        K = 1 << position
        notA = 0xfefefefefefefefe
        notH = 0x7f7f7f7f7f7f7f7f
        board = 0xffffffffffffffff
        Ka = K & notA
        Kh = K & notH

        mask = ((Ka << 7) | (K << 8) | (Kh << 9) |
                (Ka >> 1) |            (Kh << 1) |
                (Ka >> 9) | (K >> 8) | (Kh >> 7) )

        mask &= board

        return mask

