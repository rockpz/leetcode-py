# Source : https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
# Author : Ping Zhen
# Date   : 2017-04-17

'''********************************************************************************** 
* 
* Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
* An example is the root-to-leaf path 1->2->3 which represents the number 123.
* 
* Find the total sum of all root-to-leaf numbers.
* 
* For example,
* 
*     1
*    / \
*   2   3
* 
* The root-to-leaf path 1->2 represents the number 12.
* The root-to-leaf path 1->3 represents the number 13.
* 
* Return the sum = 12 + 13 = 25.
* 
*               
**********************************************************************************'''

'''
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
'''