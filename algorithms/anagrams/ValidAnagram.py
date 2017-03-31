# Source : https://leetcode.com/problems/valid-anagram/
# Author : Ping Zhen
# Date   : 2017-03-31

'''********************************************************************************** 
 * 
 * Given two strings s and t, write a function to determine if t is an anagram of s. 
 * 
 * For example,
 * s = "anagram", t = "nagaram", return true.
 * s = "rat", t = "car", return false.
 * 
 * Note:
 * You may assume the string contains only lowercase alphabets.
 *               
 **********************************************************************************'''


def isValidAnagram(strA, strB):
    if ''.join(sorted(strA)) == ''.join(sorted(strB)):
        return True
    return False

if __name__ == '__main__':
    a = 'anagram'
    b = 'nagaram'
    print(isValidAnagram(a, b))