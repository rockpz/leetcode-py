# Source : https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Author : Ping Zhen
# Date   : 2017-04-06

'''*************************************************************************************** 
 *
 * You are given an integer array nums and you have to return a new counts array. The 
 * counts array has the property where counts[i] is the number of smaller elements to 
 * the right of nums[i].
 * 
 * Example:
 * 
 * Given nums = [5, 2, 6, 1]
 * 
 * To the right of 5 there are 2 smaller elements (2 and 1).
 * To the right of 2 there is only 1 smaller element (1).
 * To the right of 6 there is 1 smaller element (1).
 * To the right of 1 there is 0 smaller element.
 * 
 * Return the array [2, 1, 1, 0].
 * 
 ***************************************************************************************'''


# The following idea is based on a `Binary Index Tree` or 'Fenwick Tree'
# There are two articles explaining this technique quite well:
# 1) http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# 2) http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
