import sys

sys.path.append('./tester')
sys.path.append('./pieces')

from Tester import Tester
from BitsTestingAdapter import BitsTestingAdapter
from KingPiece import KingPiece
from KnightPiece import KnightPiece
from RookPiece import RookPiece
from BishopPiece import BishopPiece
from QueenPiece import QueenPiece

reportTrueDetails = """
    ----
    Позация фигуры: {input}

    Количество возможных ходов и
    битовая маска всех возможных ходов короля: 
    {computed}
    ----
"""

reportFalseDetails = """
    ----
    Позация фигуры: {input}

    Количество возможных ходов и
    битовая маска всех возможных ходов фигуры

    - ожидаемый результат: 
    {expected}

    - расчетный результат: 
    {computed}
    ----
"""

# mode - варианты подсчета единичных битов в числе:
# 1 - вариант 1
# count = 0
# while (mask > 0):
#     if mask & 1 > 0:
#         count += 1
#     mask >>= 1

# 2 - вариант 2
# count = 0
# while (mask > 0):
#     count += 1
#     mask &= mask - 1

# default - через кэширование

tester0 = Tester(BitsTestingAdapter(KingPiece(), KingPiece, mode = 1), readOutputSingleLine = False)
tester1 = Tester(BitsTestingAdapter(KingPiece(), KingPiece, mode = 2), readOutputSingleLine = False)
tester2 = Tester(BitsTestingAdapter(KnightPiece(), KnightPiece, mode = 2), readOutputSingleLine = False)
tester3 = Tester(BitsTestingAdapter(KnightPiece(), KnightPiece), readOutputSingleLine = False)
tester4 = Tester(BitsTestingAdapter(RookPiece(), RookPiece), readOutputSingleLine = False)
tester5 = Tester(BitsTestingAdapter(BishopPiece(), BishopPiece), readOutputSingleLine = False)
tester6 = Tester(BitsTestingAdapter(QueenPiece(), QueenPiece), readOutputSingleLine = False)

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester1.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester2.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester3.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester4.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester5.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester6.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

# tester0.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV0.01.txt')
# tester1.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV1.01.txt')
# tester2.testdir('./tests/0.BITS/2.Bitboard - Конь', './report/0.BITS.2.Bitboard.Knight.report.popcountV1.01.txt')
# tester3.testdir('./tests/0.BITS/2.Bitboard - Конь', './report/0.BITS.2.Bitboard.Knight.report.popcountV2.01.txt')
# tester4.testdir('./tests/0.BITS/3.Bitboard - Ладья', './report/0.BITS.3.Bitboard.Rook.report.popcountV2.01.txt')
# tester5.testdir('./tests/0.BITS/4.Bitboard - Слон', './report/0.BITS.4.Bitboard.Bishop.report.popcountV2.01.txt')
tester6.testdir('./tests/0.BITS/5.Bitboard - Ферзь', './report/0.BITS.5.Bitboard.Queen.report.popcountV2.01.txt')

