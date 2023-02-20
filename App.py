import sys

sys.path.append('./tester')
sys.path.append('./pieces')

from Tester import Tester
from BitsTestingAdapter import BitsTestingAdapter
from KingPiece import KingPiece
from KnightPiece import KnightPiece

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

tester0 = Tester(BitsTestingAdapter(KingPiece(), KingPiece, mode = 1), readOutputSingleLine = False)
tester1 = Tester(BitsTestingAdapter(KingPiece(), KingPiece, mode = 2), readOutputSingleLine = False)
tester2 = Tester(BitsTestingAdapter(KnightPiece(), KnightPiece, mode = 2), readOutputSingleLine = False)
tester3 = Tester(BitsTestingAdapter(KnightPiece(), KnightPiece), readOutputSingleLine = False)

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester1.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester2.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester3.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

# tester0.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV0.01.txt')
# tester1.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV1.01.txt')
# tester2.testdir('./tests/0.BITS/2.Bitboard - Конь', './report/0.BITS.2.Bitboard.Knight.report.popcountV1.01.txt')
tester3.testdir('./tests/0.BITS/2.Bitboard - Конь', './report/0.BITS.2.Bitboard.Knight.report.popcountV3.01.txt')
