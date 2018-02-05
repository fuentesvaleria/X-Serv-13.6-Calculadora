#!/usr/bin/python3

import sys


if sys.argv[1]=='+':
	print(int(sys.argv[2]) + int(sys.argv[3]))
elif sys.argv[1]=='-':
	print(int(sys.argv[2]) - int(sys.argv[3]))
elif sys.argv[1]=='x':
	print(int(sys.argv[2]) * int(sys.argv[3]))
elif sys.argv[1]==':':
	try:
		print(int(sys.argv[2]) / int(sys.argv[3]))
	except ZeroDivisionError:
		print('no se puede dividir entre cero')	
		sys.exit()
else:
	print('introduce de nuevo el operando')
	sys.exit()

sys.exit()

