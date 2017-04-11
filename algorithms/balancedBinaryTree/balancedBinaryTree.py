# Source : https://oj.leetcode.com/problems/balanced-binary-tree/
# Author : Ping Zhen
# Date   : 2017-04-01

'''********************************************************************************** 
* 
* Given a binary tree, determine if it is height-balanced.
* 
* For this problem, a height-balanced binary tree is defined as a binary tree in which 
* the depth of the two subtrees of every node never differ by more than 1.
* 
*               
**********************************************************************************'''

'''
树的遍历主要有两种，一种是深度优先遍历， 像前序、中序、后序；另一种是广度优先遍历，像层次遍历。
在树结构中两者的区别还不是非常明显，但从树扩展到有向图，到无向图的时候，深度优先搜索和广度优先搜索的效率和作用还是有很大不同的
深度优先一般用递归，广度优先一般用队列。一般情况下能用递归实现的算法大部分也能用堆栈来实现

平衡二叉树
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

python 二叉树模块  bintrees
'''

'''
calss Node():
  def __init__(self, value=None):
    self.value = value
    self.left  = None
    self.right = None
'''
import math
from bintrees import BinaryTree

def isBalance(binTree):
  height = 0
  return isBalanceUtil(binTree.root, height)

def isBalanceUtil(node, height)
  if node is None
    height = 0
    return True

  lh = 0
  rh = 0
  isleft  = isBalanceUtil(node.left, lh)
  isright = isBalanceUtil(node.right, rh)
  if lh > rh:
    height = lh + 1
  else:
    height = rh + 1
  return math.abs(lh - rh) <= 1 and isleft and isright


  