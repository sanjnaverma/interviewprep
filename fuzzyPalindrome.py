#Write a function that returns whether or not two strings are fuzzy palindromes of one another (i.e. ignore spaces and capitalization).  
import re
import string
def isFuzzyPalindrome(a, b): # will return a boolean
	#a and b are two strings

	#first edge case, the strings must be of the same length
	if(len(a) != len(b) or len(a) == None or len(b) == None):
		print("Not fuzzy palindromes")
		return False

	else:
		#normalize the two strings
		a = a.lower()
		b = b.lower()

		a = re.sub('[^0-9a-zA-Z]+', '', a)
		b = re.sub('[^0-9a-zA-Z]+', '', b)

		

		#the characters of the a in chronological order must be the same as the reverse chronological order of b
		#reverse b
		b = b[::-1]

		if(a == b):
			return True
		else:
			return False



print(isFuzzyPalindrome("hello", "olleh"))
print(isFuzzyPalindrome("world", "world"))

#took 12 minutes to do this


