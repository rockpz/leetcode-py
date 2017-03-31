# Source : https://oj.leetcode.com/problems/add-binary/
# Author : Ping Zhen
# Date   : 2017-03-31

'''********************************************************************************** 
* 
* Given two binary strings, return their sum (also a binary string).
* 
* For example,
* a = "11"
* b = "1"
* Return "100".
* 
*               
**********************************************************************************'''

'''
python 位运算
按位与     &
按位并    ｜
按位异或   ^
按位翻转   ～
左移运算符 <<
右移运算符 >>

python 字符串操作

'''

def addBinary(strA, strB):
    add    = '0'
    result = ''
    lenA   = len(strA)
    lenB   = len(strB)
    length = 0
    if(lenA > lenB):
        length = lenA
        strB = '0' * (lenA - lenB) + strB
    else:
        length = lenB
        strA = '0' * (lenB - lenA) + strA 

    for i in range(length - 1, -1, -1):
        tmpStr = ''
        if(strA[i] == '0' and strB[i] == '0'):
            result = add + result 
            add = '0'
        elif(strA[i] == '0' and strB[i] == '1'):
            result = ((add == '1') and '0' or '1') + result
            add = (add == '1') and '1' or '0'
        elif(strA[i] == '1' and strB[i] == '0'):
            result = ((add == '1') and '0' or '1') + result
            add = (add == '1') and '1' or '0'
        else:
            result = add + result
            add = '1'
    if(add == '1'):
        result = '1' + result
    return result

if __name__ == '__main__':
    a = '11001'
    b = '111111000000000001'
    result = addBinary(a, b)
    print('addBinary ', a, " + " , b, " = ", result)