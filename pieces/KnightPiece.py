from BasePiece import BasePiece

class KnightPiece(BasePiece):
    def getMoves(self, position:int):
        K = 1 << position
        notA = 0xfefefefefefefefe
        notB = 0xfcfcfcfcfcfcfcfc
        notH = 0x7f7f7f7f7f7f7f7f
        notJ = 0x3f3f3f3f3f3f3f3f
        Ka = K & notA
        Kb = K & notB
        Kh = K & notH
        Kj = K & notJ

        mask = (             (Ka << 15) | (Kh << 17) |
                (Kb << 6)  |                        (Kj << 10) |
                (Kb >> 10) |                        (Kj >> 6)  |
                             (Ka >> 17) | (Kh >> 15) )

        return KnightPiece.normalizeMask(mask)

