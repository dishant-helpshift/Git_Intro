def getFizzBuzzUptoN( n ):
	fizzbuzzSeq = []
	for i in range( 1, n+1):
		tmpstr = ""
		if i%3==0:
			tmpstr += "Fizz"
		if i%5==0:
			tmpstr += "Buzz"
		if tmpstr == "":
			tmpstr = tmpstr + str(i)
		fizzbuzzSeq.append( tmpstr )
	return fizzbuzzSeq

if __name__ == "__main__":
	fizzbuzzSeq = getFizzBuzzUptoN( 10 )
	print(fizzbuzzSeq)