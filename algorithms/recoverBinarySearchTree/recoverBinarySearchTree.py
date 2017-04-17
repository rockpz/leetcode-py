# Source : https://oj.leetcode.com/problems/recover-binary-search-tree/
# Author : Ping Zhen
# Date   : 2017-04-17

'''********************************************************************************** 
* 
* Two elements of a binary search tree (BST) are swapped by mistake.
* 
* Recover the tree without changing its structure.
* 
* Note:
* A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
* 
* confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
* 
* OJ's Binary Tree Serialization:
* 
* The serialization of a binary tree follows a level order traversal, where '#' signifies 
* a path terminator where no node exists below.
* 
* Here's an example:
* 
*    1
*   / \
*  2   3
*     /
*    4
*     \
*      5
* 
* The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}". 
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

'''
 We can convert the BST to a sorted array,  then we can find the two nodes which missed the order.

 To cover the BST to sorted array, we needn't use an extra array, we just traverse the tree in order.
  
                   8
           _______/ \_______
          /                 \
         4                  12
      __/ \__             __/ \__
     /       \           /       \
    2         6        10        14
   / \       / \       / \       / \
  1   3     5   7     9  11    13  15
''' 
  