# Source : https://oj.leetcode.com/problems/linked-list-cycle/
# Author : Ping Zhen
# Date   : 2017-04-14

'''********************************************************************************** 
* 
* Given a linked list, determine if it has a cycle in it.
* 
* Follow up:
* Can you solve it without using extra space?
* 
*               
**********************************************************************************'''

'''
 * if there is a cycle in the list, then we can use two pointers travers the list.
 *
 * one pointer traverse one step each time, another one traverse two steps each time.
 *
 * so, those two pointers meet together, that means there must be a cycle inside the list.
'''