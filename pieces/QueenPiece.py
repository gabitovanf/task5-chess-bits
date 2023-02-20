from BishopPiece import BishopPiece
from RookPiece import RookPiece
from BasePiece import BasePiece

class QueenPiece(BasePiece):
    def __init__(self):
        self.__rook = RookPiece()
        self.__bishop = BishopPiece()

    def getMoves(self, position:int):
        maskBishop = self.__bishop.getMoves(position)
        maskRook = self.__rook.getMoves(position)

        return maskBishop | maskRook

