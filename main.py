import sys
import os


def add(addend, addend1):
	# Enter addition code here
	print("")

def sub(first, second):
	# Enter subtraction code here
	print("")

def multi(multiplicand, multiplier):
	# Enter multiplication code here
	print("")

def div(dividend, divisor):
	# Enter division code here
	print("")

if __name__ == "__main__":
	print ("Calculator")
	print ("A. Addition")
	print ("B. Subtraction")
	print ("C. Multiplication")
	print ("D. Division")
	print ("Please choose what operation to perform: ")
	opt = input().upper()
	os.system('clear')
	print ("Enter first operand: ")
	x = int(input())
	print ("Enter second operand: ")
	y = int(input())
	if opt == 'A':
		add(x,y)
	elif opt == 'B':
		sub(x,y)
	elif opt == 'C':
		multi(x,y)
	elif opt == 'D':
		div(x, y)
#try
