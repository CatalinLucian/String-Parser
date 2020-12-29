import sys

"""
Checks if string str1 is suffix of string str2 
:param str1: first string   
:param str2: second string
:return: returns 0 if str1 is not suffix of str2, len(str1) otherwise
"""
def is_suffix(str1, str2):

    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        return 0
    for i in range(len1):
        if str1[len1 - i - 1] != str2[len2 - i - 1]:
            return 0
    return len1

    """
    Computes the longest string match between prefix of pattern and suffix of new string
    :param pattern: pattern (string)
    :param new_string: new_string (the other string)
    :return: the max number of characters matched
    """
def longest_match(pattern, new_string):
    len1 = len(pattern)
    len2 = len(new_string)
    count = 0
    max = 0
    # take every prefix of pattern and see if it is suffix of new_string
    # return the maximum length prefix
    for i in range(len1):
        if is_suffix(pattern[:(i + 1)], new_string) != 0:
            count = is_suffix(pattern[:(i + 1)], new_string)
            if count > max:
                max = count
    return max

    """

    :param p: 
    :return: 
    """

def compute_delta(p):
    delta = {}
    # consider the universal alphabet for every case
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # initialize delta
    for i in range(len(p) + 1):
        for j in alphabet:
            delta[i, j] = 0
    for i in range(len(p) + 1):
        for j in alphabet:
            #extract the prefix from pattern
            prefix = p[:i]
            # form the new string by appending the current letter to the current state
            new_string = prefix + j
            # compute delta[i][j]
            delta[i, j] = longest_match(p, new_string)
    return delta

def automata_matcher(p, t, file):
    q = 0
    delta = compute_delta(p)
    for i in range(len(t)):
        q = delta[q, t[i]]
        if q == len(p):
            file.write(str(i - (len(p) - 1)) + " ")


if __name__ == '__main__':
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w")
    input = input_file.read().splitlines()
    pattern = input[0]
    text = input[1]
    automata_matcher(pattern, text, output_file)
    output_file.write('\n')
    input_file.close()
    output_file.close()

