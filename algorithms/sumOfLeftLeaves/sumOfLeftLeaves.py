# Source : https://leetcode.com/problems/sum-of-left-leaves/
# Author : Ping Zhen 
# Date   : 2017-04-17

'''*************************************************************************************** 
 *
 * Find the sum of all left leaves in a given binary tree.
 * 
 * Example:
 * 
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
 * 
 * There are two left leaves in the binary tree, with values 9 and 15 respectively. 
 * Return 24.
 ***************************************************************************************'''

'''
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
'''