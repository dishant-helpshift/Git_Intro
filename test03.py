import code03 as codes

def runTest( fun, input, output ):
	actualOutput = fun( input )
	return actualOutput, actualOutput == output

def runTestSuite( fun, testSuite ):
	for input, output in testSuite.items():
		actualOutput, status = runTest( fun, input, output )
		print("Input: ", input )
		print("Exp. output: ", output)
		print("Act. output: ", actualOutput)
		print("Test Status: ", status)
		print('')

if __name__ == "__main__":
	freqTestSuite = {
		"a a b b b c":{'a':2, 'b':3, 'c':1 },
		"a b c c c":{'a':1, 'b':1, 'c':3 },
		"a a  a":{'a':3 },
		"a  b  c  c":{'a':1, 'b':1, 'c':2 },
		"quick fox lazy dog quick donkey fire fox":{"quick": 2, "fox": 2, "lazy": 1, "dog": 1, "donkey": 1, "fire": 1} 
	}
	runTestSuite( codes.getFrequencyDict, freqTestSuite )