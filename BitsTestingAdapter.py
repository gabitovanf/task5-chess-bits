import sys
import time

sys.path.append('./tester')

from TestingInstanceInterface import TestingInstanceInterface, compareFloat, getNumDigits

class BitsTestingAdapter(TestingInstanceInterface):
    def __init__(self, instance, instanceClass, mode = 0):
        self.instance = instance
        self.instanceClass = instanceClass
        self.mode = mode

    def compute(self, *input) -> dict:
        print('Start with', input)

        try:
            firstInputVal = input[0]
            firstInputVal = int(firstInputVal)
            mask = self.instance.getMoves(firstInputVal)
            popCount = self.instanceClass.popcount(mask, self.mode)
            computed = { "count": popCount, "moves": mask }

        except ValueError as e:
            computed = { "message": 'Invalid input data' }
            print(e)

        except AttributeError as e:
            computed = { "message": 'Instance or class passed is invalid: it must contain a method .getNumPrimes(inputValue:int)' }
            print(e)

        except Exception as e:
            code = e.__class__.__name__
            computed = { "message": f"Exception occured: {code} {e}" }
            print(e)

        print('End with', computed)
        
        return computed

    def validate(self, *input, output = '') -> dict:
        starttime = time.time()
        computedDict = self.compute(*input)
        secondsPassed = time.time() - starttime

        print(computedDict, computedDict.values())
        print([str(val) for val in computedDict.values()])

        inputList = list(map(lambda x: int(x), input))
        input0 = None
        if len(inputList) > 0: input0 = inputList[0]

        computed = '\n'.join([str(val) for val in computedDict.values()])
        outputString = '\n'.join([str(int(val)) for val in output])

        return ({ 
            "valid": computed == outputString, 
            "computed": computed, 
            "expected": outputString, 
            "seconds": secondsPassed,
            "input": input0
        })

    def getEntityName(self) -> str:
        return self.instance.__class__.__name__

        