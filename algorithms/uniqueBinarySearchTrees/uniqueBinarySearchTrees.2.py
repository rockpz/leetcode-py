# Source : https://oj.leetcode.com/problems/unique-binary-search-trees-ii/
# Author : Ping Zhen
# Date   : 2017-04-17

'''********************************************************************************** 
* 
* Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
* 
* For example,
* Given n = 3, your program should return all 5 unique BST's shown below.
* 
*    1         3     3      2      1
*     \       /     /      / \      \
*      3     2     1      1   3      2
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