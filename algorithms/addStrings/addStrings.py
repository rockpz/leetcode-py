# Source : https://leetcode.com/problems/add-strings/
# Author : Ping Zhen
# Date   : 2017-03-31

'''*************************************************************************************** 
 *
 * Given two non-negative numbers num1 and num2 represented as string, return the sum 
 * of num1 and num2.
 * 
 * Note:
 * 
 * The length of both num1 and num2 is 
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to integer 
 * directly.
 ***************************************************************************************'''

import math

def addStrings(strA, strB):
    lengthA = len(strA)
    lengthB = len(strB)
    flag   = 0
    length = 0
    result = ''
    if lengthA > lengthB:
        length = lengthA
        strB = '0' * (lengthA - lengthB) + strB
    else:
        length = lengthB
        strA = '0' * (lengthB - lengthA) + strA

    for i in range(length-1, -1, -1):
        a = int(strA[i])
        b = int(strB[i])
        total = a + b + flag
        result = str(total%10) + result
        #print(a, b, flag, total, result)
        flag   = math.floor(total / 10)
    if flag:
        result = str(flag) + result
    return result

if __name__ == '__main__':
    a = '13466'
    b = '762'
    result = addStrings(a, b)
    print(a, ' and ', b, ' add strings result is ', result)