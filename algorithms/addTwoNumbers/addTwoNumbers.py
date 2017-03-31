# Source : https://leetcode.com/problems/add-strings/
# Author : Ping Zhen
# Date   : 2017-03-31

'''*************************************************************************************** 
 *
 * Given two non-negative numbers num1 and num2 represented as string, return the sum 
 * of num1 and num2.
 * 
 * Note:
 * 
 * The length of both num1 and num2 is 
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to integer 
 * directly.
 ***************************************************************************************'''

'''
python 链表实现
'''

class Node():
    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode

class NodeList():
    def __init__(self):
        self.rootPoint = None
        #self.lastPoint = None

    def insert(self, n):
        if not isinstance(n, Node):
            n = Node(n)
        if self.rootPoint is None:
            self.rootPoint = n
        else:
            a = self.rootPoint
            while isinstance(a._nextnode, Node):
                a = a._nextnode
            a._nextnode = n

    def printList(self):
        nextNode = self.rootPoint
        while isinstance(nextNode, Node):
            print(nextNode.value)
            nextNode = nextNode._nextnode
        print(nextNode)

def addTwoNumbers(listA, listB):
    c = NodeList()

    a = listA.rootPoint
    b = listB.rootPoint
    while isinstance(a, Node) or isinstance(b, Node):
        numA = 0
        numB = 0
        if isinstance(a, Node):
            numA = a.value
            a    = a._nextnode
        if(isinstance(b, Node)):
            numB = b.value
            b    = b._nextnode
        c.insert(numA + numB)

    return c


if __name__ == '__main__':
    a = NodeList()
    a.insert(3)
    a.insert(0)
    #a.insert(7)
    a.printList()
    b = NodeList()
    b.insert(7)
    b.insert(5)
    b.insert(4)
    b.printList()
    result = addTwoNumbers(a, b)
    print(result)
    result.printList()
        

