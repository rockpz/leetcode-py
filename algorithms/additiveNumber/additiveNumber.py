# Source : https://leetcode.com/problems/additive-number/
# Author : Ping Zhen
# Date   : 2017-03-31

'''*************************************************************************************** 
 *
 * Additive number is a positive integer whose digits can form additive sequence.
 * 
 * A valid additive sequence should contain at least three numbers. Except for the 
 * first two numbers, each subsequent number in the sequence must be the sum of the 
 * preceding two.
 * 
 * For example:
 * "112358" is an additive number because the digits can form an additive sequence: 1, 
 * 1, 2, 3, 5, 8.
 * 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
 * "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
 * 1 + 99 = 100, 99 + 100 = 199
 * 
 * Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 
 * 03 or 1, 02, 3 is invalid.
 * 
 * Given a string represents an integer, write a function to determine if it's an 
 * additive number.
 * 
 * Follow up:
 * How would you handle overflow for very large input integers?
 * 
 * Credits:Special thanks to @jeantimex for adding this problem and creating all test 
 * cases.
 *               
 ***************************************************************************************'''

 '''
 python itertools 库
 '''

import itertools
 

def isAdditiveNumber(strNum):
    length = len(strNum)
    for i, j in itertools.combinations(range(1, length), 2):
        a = strNum[:i]
        b = strNum[i:j]
        if a[0] == '0' or b[0] == '0':
            continue
        while j < length:
            c = str(int(a) + int(b))
            if not strNum.startswith(c, j):
                break
            j = j + len(c)
            a = b
            b = c
        if j == length:
            return True
    return False

if __name__  == "__main__":
    a = '11235812'
    result = isAdditiveNumber(a)
    print(a, ' juge additive number is ', result)






