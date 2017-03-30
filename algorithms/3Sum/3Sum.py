# Source : https://oj.leetcode.com/problems/3sum/
# Author : Ping Zhen
# Date   : 2017-03-28

'''********************************************************************************** 
* 
* Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
* Find all unique triplets in the array which gives the sum of zero.
* 
* Note:
* 
* Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
* The solution set must not contain duplicate triplets.
* 
*     For example, given array S = {-1 0 1 2 -1 -4},
* 
*     A solution set is:
*     (-1, 0, 1)
*     (-1, -1, 2)
* 
*               
**********************************************************************************'''

'''*
 *   Simlar like "Two Number" problem, we can have the simlar solution.
 *
 *   Suppose the input array is S[0..n-1], 3SUM can be solved in O(n^2) time on average by 
 *   inserting each number S[i] into a hash table, and then for each index i and j,  
 *   checking whether the hash table contains the integer - (s[i]+s[j])
 *
 *   Alternatively, the algorithm below first sorts the input array and then tests all 
 *   possible pairs in a careful order that avoids the need to binary search for the pairs 
 *   in the sorted list, achieving worst-case O(n^n)
 *
 *   Solution:  Quadratic algorithm
 *   http://en.wikipedia.org/wiki/3SUM
 *
 *'''
# python sort  list length   for while if else if
'''
li = [1,2,3,4,5,7];
sum = 10;
len = li.len
result = [];
for (i= 0; i < len - 2 ; i ++)
    if(i > 0 and li[i] == li[i-1]) continue
    low = i + 1
    high = len - 1

    while(low < high):
        a = li[i]
        b = li[low]
        c = li[high]
        if(a + b + c = sum):
            result.push([a, b ,c])
            low++
            high--
        elif (a + b + c > sum):
            high--
        else:
            low++
return result
'''


def threeSum(li, target):
    li.sort()
    print(li)
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
                result.append([a, b ,c])
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

def printResult(result):
	print("A solution set is : ", result)

if __name__ == '__main__':
    inputList = [-1, 1, 2, 1, -1, -1, 0, 0, 0]
    result = threeSum(inputList, 0)
    printResult(result)
