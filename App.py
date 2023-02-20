import sys

sys.path.append('./tester')
sys.path.append('./pieces')

from Tester import Tester
from BitsTestingAdapter import BitsTestingAdapter
from KingPiece import KingPiece

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

tester0 = Tester(BitsTestingAdapter(KingPiece(), KingPiece), readOutputSingleLine = False)
tester1 = Tester(BitsTestingAdapter(KingPiece(), KingPiece, mode = 1), readOutputSingleLine = False)

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester1.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

# tester0.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV0.01.txt')
tester1.testdir('./tests/0.BITS/1.Bitboard - Король', './report/0.BITS.1.Bitboard.King.report.popcountV1.01.txt')
