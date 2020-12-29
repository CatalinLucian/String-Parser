
			Parser for strings

	Boyer-Moore is the algorithm implemented in the project. Its main 
use is in the searching of one string within another string using a good
time complexity.

	The implementation of the algorithm is very straight-forward.
I implemented the 'automata_matcher' pseudocod for the algorithm presented in
the class course. The 'delta' transition matrix was the bread and butter of the
algorithm. 
	To represent 'delta' I considered a dictionary with double key:
   * the first key i simulates the state or the length of every prefix from my 
     pattern
   * the second key j simulates every letter from the English alphabe
   * the correspondent value simulates the lenght of the longest suffix of
     i.append(j) which is prefix for i 
	To compute every value I considered every element from 'delta' and I 
found the longest possible match between every prefix and every new word
formed by appending letters of the alphabet to the prefixes considered.
	The helper functions are:
   * isSuffix(a, b) - checks if a is suffix for b
   * longest_match(pattern, new_string) - iterates through every prefix of
     'pattern' and with 'isSuffix' check if the actual prefix is suffix for
     'new_string'
     - out of all the posibilities it returns the maximum-length one
     - this are the values which with 'delta' should be populated 			
	
	For the coding style I used the 4 spaces identation convention recognized
by Python.
