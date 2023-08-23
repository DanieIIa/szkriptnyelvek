#!/usr/bin/env python3

import time
import os
import sys


DIGITS = [
	[" ┏━┓ ", "  ╻  ", " ┏━┓ ", " ┏━┓ ", " ╻ ╻ ", " ┏━┓ ", " ┏   ", " ┏━┓ ", " ┏━┓ ", " ┏━┓ ", "   "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", " ╻ "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┏━┛ ", " ┣━┫ ", " ┗━┫ ", " ┗━┓ ", " ┣━┓ ", "   ┃ ", " ┣━┫ ", " ┗━┫ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ╹ "],
	[" ┗━┛ ", "  ╹  ", " ┗━━ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   "],
]

def main():
	format = "%H:%M:%S"
	if len(sys.argv) > 1:
		format = "%H:%M"
		for index in range(0,len(sys.argv[1]),1):
			if(sys.argv[1][index] == "s"):
				format = "%H:%M:%S"
	print("_"*15)
	while(True):
		
		os.system("cls")
		str_time = time.strftime(format, time.localtime())
		for i in range(0,7,1):
			for s in range(0, len(str_time),1):
				if(str_time[s] != ":"):
					print(DIGITS[i][int(str_time[s])], end="")
				else:
					print(DIGITS[i][10], end="")		
			print()
		time.sleep(1)
		
    
    
if __name__ == "__main__":
    main()