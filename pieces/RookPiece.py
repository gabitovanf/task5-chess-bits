from BasePiece import BasePiece

class RookPiece(BasePiece):
    def getMoves(self, position:int):
        V = 0x101010101010101
        H = 0xff                    # i.e. 255
        
        Rv = V << (position % 8)
        Rh = H << (position - position % 8)

        mask = Rv ^ Rh

        return RookPiece.normalizeMask(mask)

