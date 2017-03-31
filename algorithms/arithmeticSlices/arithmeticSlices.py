# Source : https://leetcode.com/problems/arithmetic-slices/
# Author : Ping Zhen
# Date   : 2017-03-31

'''*************************************************************************************** 
 *
 * A sequence of number is called arithmetic if it consists of at least three elements 
 * and if the difference between any two consecutive elements is the same.
 * 
 * For example, these are arithmetic sequence:
 * 1, 3, 5, 7, 9
 * 7, 7, 7, 7
 * 3, -1, -5, -9
 * 
 * The following sequence is not arithmetic. 1, 1, 2, 5, 7 
 * 
 * A zero-indexed array A consisting of N numbers is given. A slice of that array is 
 * any pair of integers (P, Q) such that 0 
 * 
 * A slice (P, Q) of array A is called arithmetic if the sequence:
 *     A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means 
 * that P + 1 
 * 
 * The function should return the number of arithmetic slices in the array A. 
 * 
 * Example:
 * 
 * A = [1, 2, 3, 4]
 * 
 * return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] 
 * itself.
 ***************************************************************************************'''

import copy
import math

def arithmeticSlices(li):
    arithmeticList = []
    sequence = []
    i = 0
    while i < len(li):
        if len(sequence) == 0:
            sequence.append(li[i])
            i = i + 1
        elif len(sequence) == 1:
            sequence.append(li[i])
            i = i + 1
        else:
            #print(i, li[i], sequence[-1], sequence[1], sequence[0])
            if (sequence[1] - sequence[0]) == (li[i] - sequence[-1]):
                sequence.append(li[i])
                #print("sequence is ", sequence)
                i = i + 1
            else:
                if len(sequence) >= 3:
                    arithmeticList.append(copy.deepcopy(sequence))
                sequence = []
                i = i - 1
    if len(sequence) >= 3:
        arithmeticList.append(sequence)

    #print(arithmeticList)

    count = 0
    for arithmeticSequence in arithmeticList:
        if arithmeticSequence[1] - arithmeticSequence[0] == 0:
            count = count + len(arithmeticSequence) - 2
        else:
            count = count + math.floor((len(arithmeticSequence) - 1) * (len(arithmeticSequence) - 2) /2)
    return count


if __name__ == '__main__':
    a = [1, 2, 3, 4, 6, 8, 10, 12, 14]
    result = arithmeticSlices(a)
    print(a, ' arithmeticSlices  count is ', result)



