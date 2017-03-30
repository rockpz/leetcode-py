# Source : https://oj.leetcode.com/problems/3sum-closest/
# Author : Ping Zhen
# Date   : 2017-03-30

'''********************************************************************************** 
* 
* Given an array S of n integers, find three integers in S such that the sum is 
* closest to a given number, target. Return the sum of the three integers. 
* You may assume that each input would have exactly one solution.
* 
*     For example, given array S = {-1 2 1 -4}, and target = 1.
* 
*     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
* 
*               
**********************************************************************************'''

#solution:  http://en.wikipedia.org/wiki/3SUM
#the idea as blow:
#  1) sort the array.
#  2) take the element one by one, calculate the two numbers in reset array.
#
#notes: be careful the duplication number.
#
# for example:
#    [-4,-1,-1,1,2]    target=1
# 
#    take -4, can cacluate the "two number problem" of the reset array [-1,-1,1,2] while target=5
#    [(-4),-1,-1,1,2]  target=5  distance=4
#           ^      ^ 
#    because the -1+2 = 1 which < 5, then move the `low` pointer(skip the duplication)
#    [(-4),-1,-1,1,2]  target=5  distance=2
#                ^ ^ 
#    take -1(skip the duplication), can cacluate the "two number problem" of the reset array [1,2] while target=2
#    [-4,-1,(-1),1,2]  target=2  distance=1
#                ^ ^ 

import sys

def threeSumCloset(li, target):
    if(len(li) < 3): 
        return 'list length < 3!'
           
    li.sort()
    length = len(li)
    distance = sys.maxsize
    if(li[0] + li[1] + li[2] > target): 
        return abs(li[0] + li[1] + li[2] - target)
    if(li[length-1] + li[length-2] + li[length-3] < target):
        return abs(li[length-1] + li[length-2] + li[length-3] - target)
    for i in (0, length -2):
        if(i > 0 and li[i] == li[i - 1]): continue
        a = li[i]
        lowIndex  = i + 1
        highIndex = length - 1

        while(highIndex > lowIndex):
            b = li[lowIndex]
            c = li[highIndex]
            sum = a + li[lowIndex] + li[highIndex]

            if(sum == target):
                return 0
            else:
                if(abs(sum - target) < distance):
                    distance = abs(sum - target)
                if(sum > target):
                    while(highIndex > lowIndex and li[highIndex] == li[highIndex - 1]):
                        highIndex = highIndex - 1
                    highIndex = highIndex - 1
                else:
                    while(highIndex > lowIndex and li[lowIndex] == li[lowIndex + 1]):
                        lowIndex = lowIndex + 1
                    lowIndex = lowIndex + 1

    return distance


if __name__ == '__main__':
    inputList = [1,6,8,9,-1,3,14]
    distance  = threeSumCloset(inputList, 10)
    print(distance)