# Source : https://oj.leetcode.com/problems/4sum/
# Author : Ping Zhen
# Date   : 2017-03-30

'''********************************************************************************** 
* 
* Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
* Find all unique quadruplets in the array which gives the sum of target.
* 
* Note:
* 
* Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
* The solution set must not contain duplicate quadruplets.
* 
*     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
* 
*     A solution set is:
*     (-1,  0, 0, 1)
*     (-2, -1, 1, 2)
*     (-2,  0, 0, 2)
* 
*               
**********************************************************************************'''

def fourSum(li, target):
    if(len(li) < 4): return []
    li.sort()
    result = []
    for i in range(0, len(li) - 3):
        stepResult = threeSum(li[i+1:], target-li[i], li[i])
        result.extend(stepResult)
    return result

def threeSum(li, target, prefix):
    result = []
    length = len(li)
    for i in range(0, length-2):
        if(i > 0 and li[i] == li[i-1]): continue
        lowIndex   = i + 1
        highIndex  = length - 1
        while(highIndex > lowIndex):
            a = li[i]
            b = li[lowIndex]
            c = li[highIndex]

            if(a + b + c) == target:
                print(i, lowIndex, highIndex)
                result.append([prefix, a, b ,c])
                while highIndex > lowIndex and li[lowIndex] == li[lowIndex + 1]: 
                    lowIndex = lowIndex + 1
                while highIndex > lowIndex and li[highIndex] == li[highIndex - 1]:
                    highIndex = highIndex - 1
                lowIndex = lowIndex + 1
                highIndex = highIndex - 1
            elif(a + b + c) > target:
                highIndex = highIndex - 1
            else:
                lowIndex = lowIndex + 1
    return result

if __name__ == '__main__':
    inputList = [1,0,-1,0,-2,2]
    result = fourSum(inputList, 0)
    print(result)