# Source : https://oj.leetcode.com/problems/gray-code/
# Author : Ping Zhen
# Date   : 2017-04-11

'''********************************************************************************** 
* 
* The gray code is a binary numeral system where two successive values differ in only one bit.
* 
* Given a non-negative integer n representing the total number of bits in the code, 
* print the sequence of gray code. A gray code sequence must begin with 0.
* 
* For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
* 
* 00 - 0
* 01 - 1
* 11 - 3
* 10 - 2
* 
* Note:
* For a given n, a gray code sequence is not uniquely defined.
* 
* For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
* 
* For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
*               
**********************************************************************************'''

'''
 * I designed the following stupid algorithm base on the blow observation
 * 
 * I noticed I can use a `mirror-like` binary tree to figure out the gray code.
 * 
 * For example:
 * 
 *           0      
 *        __/ \__   
 *       0       1  
 *      / \     / \ 
 *     0   1   1   0
 * So, the gray code as below: (top-down, from left to right)
 *
 *     0 0 0 
 *     0 0 1
 *     0 1 1
 *     0 1 0
 * 
 *                  0
 *            _____/ \_____
 *           0             1
 *        __/ \__       __/ \__
 *       0       1     1       0
 *      / \     / \   / \     / \
 *     0   1   1   0 0   1   1   0
 * 
 * So, the gray code as below:
 *
 *     0 0 0 0 
 *     0 0 0 1
 *     0 0 1 1
 *     0 0 1 0
 *     0 1 1 0
 *     0 1 1 1 
 *     0 1 0 1
 *     0 1 0 0
'''