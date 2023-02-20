from BasePiece import BasePiece

class BishopPiece(BasePiece):
    def getMoves(self, position:int):
        DL = 0x8040201008040201     # diagon
        TL = 0x80c0e0f0f8fcfeff     # triangle
        DR = 0x102040810204080      # diagon
        TR = 0x103070f1f3f7fff      # triangle
        
        SHL = position % 8 - position // 8
        SHR = 7 - (position % 8 + position // 8)

        if SHL < 0: 
            SHL *= -8
            Bl = DL << SHL
        else:
            Bl = DL << SHL
            Bl &= TL

        if SHR < 0: 
            SHR *= -8
            Br = DR << SHR
        else:
            Br = DR >> SHR
            Br &= TR >> (SHR * 8)
        

        mask = Bl ^ Br
        
        return BishopPiece.normalizeMask(mask)

