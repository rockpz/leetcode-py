# Source : https://oj.leetcode.com/problems/copy-list-with-random-pointer/
# Author : Ping Zhen
# Date   : 2017-04-06

'''********************************************************************************** 
* 
* A linked list is given such that each node contains an additional random pointer 
* which could point to any node in the list or null.
* 
* Return a deep copy of the list.
* 
*               
**********************************************************************************'''



'''**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 *'''


'''*    
 *
 *  The idea as below:
 *
 *  Consider we have a linked list as below:
 *
 *    node1->random = node2;
 *    node2->random = node1;
 *    node3->random = node1;
 *    
 *       +-------------+                         
 *       |             v                         
 *    +-------+    +-------+    +-------+        
 *    | node1 |----> node2 |----> node3 |--->NULL
 *    +-------+    +-------+    +-------+        
 *      ^  ^           |           |             
 *      |  +-----------+           |             
 *      +--------------------------+             
 *    
 *
 *  To copy the list, 
 *   
 *    1) We insert a new node for each node's next position
 *
 * 
 *       +-------------------------+                                     
 *       |                         v                                     
 *    +--+----+     +-----+    +-------+     +-----+    +-------+     +-----+     
 *    | node1 |---> | NEW |----> node2 |---> | NEW |----> node3 |---> | NEW | ---> NULL
 *    +-------+     +-----+    +---+---+     +-----+    +--+----+     +-----+ 
 *      ^  ^                       |                       |             
 *      |  +-----------------------+                       |             
 *      +--------------------------------------------------+             
 *
 *    2) Then, we can construt the new node's random pointer:
 *
 *        (node1->next) -> random  = (node1->random) -> next;
 *
 *    3) After we take out all of the "NEW" node to finish the copy.
 *    
 *'''