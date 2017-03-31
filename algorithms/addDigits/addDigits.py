# Source : https://leetcode.com/problems/add-digits/
# Author : Ping Zhen
# Date   : 2017-03-31

'''********************************************************************************** 
 * Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
 *
 * For example:
 * Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
 *
 * Follow up:
 *  Could you do it without any loop/recursion in O(1) runtime?
 *
 **********************************************************************************'''


def addDigits(num):
    if num == 0:
        return num
    return (num - 1) % 9 + 1

if __name__ == '__main__':
    a = 234567
    result = addDigits(a)
    print(a, ' add digits result is ', result);