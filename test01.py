import code01 as codes

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
	fizzbuzzTestSuite = { 
		1:['1'], 
		2:['1','2'], 
		3:['1','2','Fizz'], 
		5:['1','2','Fizz','4','Buzz'], 
		17:['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17'] 
	}
	runTestSuite( codes.getFizzBuzzUptoN, fizzbuzzTestSuite )