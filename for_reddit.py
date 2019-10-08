from sys import argv
from crypt import crypt
from itertools import product
from colorama import Fore

def main():
	if len(argv) != 2:
		print("use with the hash")
		return 1
	salt = argv[1][0] + argv[1][1]
	#extending the valid chars with a dictionary definition
	valid_chars = ''.join([chr(i) for i in range(32, 127)])
	
	repetitions = 1
	while(True):
		for cart_prod in product(valid_chars, repeat=repetitions):
			if(crypt(''.join(cart_prod)) == argv[1]):
				print(Fore.GREEN + ''.join(cart_prod))
				return 0
			print(Fore.RED + ''.join(cart_prod))
		repetitions += 1

main()
