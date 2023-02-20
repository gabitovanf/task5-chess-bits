import os
from TestingInstanceInterface import TestingInstanceInterface

class Tester:
    __reportHeader =  """
    ОТЧЁТ О ТЕСТИРОВАНИИ {entityName}
    Директория тестовых данных: 
    {dirpath}

    --------------

    """

    __reportItem = """

    {iterationName} - {result} - {seconds} сек
    """

    __reportTrueDetails = """
    ----
    Input: {input}
    Solution: {computed}
    ----
    """

    __reportFalseDetails = """
    ----
    Input: {input}
    Expected: {expected}
    Computed: {computed}
    ----
    """

    def __init__(self, instance: TestingInstanceInterface, readOutputSingleLine:bool = True):
        self.instance = instance
        self.lastreport = ''
        self.lastreportFile = None
        self.readOutputSingleLine = readOutputSingleLine

        self._reportItem = Tester.__reportItem
        self._reportTrueDetails = Tester.__reportTrueDetails
        self._reportFalseDetails = Tester.__reportFalseDetails

    def testdir(self, dirpath:str, reportpath:str):
        # Store current location
        curdir = os.getcwd()

        try:
            self.__startNewReport(os.path.abspath(dirpath), reportpath)

            os.chdir(dirpath)

            for filenamesDict in Tester.__getFilenamesDict(os.listdir()):
                iterationName = filenamesDict['in'][0:-3]
                fileContentDict = Tester.__readFiles(filenamesDict, self.readOutputSingleLine)

                print(fileContentDict)

                # Continue if in- or out- has not been found 
                # or any other exeption raised
                if (fileContentDict == None): continue

                # Compute and compare result with out-file's content
                testResult = self.instance.validate(output = fileContentDict['out'], *fileContentDict['in'])

                print(testResult)

                self.__appendReportItem(iterationName, testResult)
        finally:
            self.__closeReport()

        print(self.lastreport)

        # Set cwd back to current
        os.chdir(curdir)

    def setupReportStrings(self, reportItem = None, reportTrueDetails = None, reportFalseDetails = None):
        if (reportItem != None): self._reportItem = reportItem
        if (reportTrueDetails != None): self._reportTrueDetails = reportTrueDetails
        if (reportFalseDetails != None): self._reportFalseDetails = reportFalseDetails

    def resetReportStrings(self, reportItem = None, reportTrueDetails = None, reportFalseDetails = None):
        self._reportItem = Tester.__reportItem
        self._reportTrueDetails = Tester.__reportTrueDetails
        self._reportFalseDetails = Tester.__reportFalseDetails

    @staticmethod
    def __getFilenamesDict(dirAndFiles:list) -> list:
        filenameList = sorted(filter(lambda filename: filename.endswith('.in'), dirAndFiles))

        return list(map(lambda filename: { "in": filename, "out": filename[0:-3] + '.out' }, filenameList))

    @staticmethod
    def __readFiles(filenamesDict:dict, readOutputSingleLine:bool = True) -> dict:
        fileContentDict = {}

        for (key, filename) in filenamesDict.items():
            try:
                with open(filename, 'r') as f:
                    if (key == 'out'):
                        if readOutputSingleLine: 
                            content = f.readline()
                            content = content.strip()
                        else:
                            content = f.readlines()
                    else:
                        content = f.readlines()

                    fileContentDict[key] = content
            except Exception as e:
                fileContentDict = None
                print(e)
                break


        return fileContentDict

    @staticmethod
    def __openNewReportFile(reportpath:str):
        curdir = os.getcwd()
        reportdir = os.path.dirname(reportpath)
        reportdirLength = len(reportdir)
        reportfile = reportpath[reportdirLength+1:]

        os.chdir(reportdir)

        f = open(reportfile, 'w') # change to 'w'

        print(f)

        os.chdir(curdir)

        return f


    def __startNewReport(self, dirpath:str, reportpath:str):
        self.lastreportFile = Tester.__openNewReportFile(reportpath)

        entityName = self.instance.getEntityName()

        header = Tester.__reportHeader.format(entityName=entityName, dirpath=dirpath)

        # Start write
        self.lastreportFile.write(header)
        self.lastreport = header

    def __appendReportItem(self, iterationName, testResult):
        self.__appendPartStr(self._reportItem
                .format(iterationName = iterationName, result = testResult['valid'], seconds = testResult['seconds']))

        if (testResult['valid'] == True):
            self.__appendPartStr(self._reportTrueDetails
                .format(**testResult))
        else:
            self.__appendPartStr(self._reportFalseDetails
                .format(**testResult))

    def __appendPartStr(self, part:str):
        self.lastreportFile.write(part)
        self.lastreport += part

    def __closeReport(self):
        if (self.lastreportFile == None):
            return

        self.lastreportFile.close()
        self.lastreportFile = None

