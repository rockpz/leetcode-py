# Source : https://oj.leetcode.com/problems/anagrams/
# Author : Ping Zhen
# Date   : 2017-03-31

'''********************************************************************************** 
 * 
 * Given an array of strings, group anagrams together.
 * 
 * For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
 * Return:
 * 
 * [
 *   ["ate", "eat","tea"],
 *   ["nat","tan"],
 *   ["bat"]
 * ]
 * 
 * Note:
 * 
 * For the return value, each inner list's elements must follow the lexicographic order.
 * All inputs will be in lower-case.
 * 
 * Update (2015-08-09):
 * The signature of the function had been updated to return list<list<string>> instead 
 * of list<string>, as suggested here. If you still see your function signature return 
 * a list<string>, please click the reload button  to reset your code definition.
 * 
 **********************************************************************************'''

'''
python 字典排序  hashMap
'''


def groupAnagrams(li):
    stepResult = {}
    for i in range(0, len(li)):
        key = ''.join(sorted(li[i]))
        if key not in stepResult:
            stepResult[key] = []
        stepResult[key].append(li[i])

    result = []
    for key in stepResult.keys():
        stepResult[key].sort()
        result.append(stepResult[key])
    return result

if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(a)
    print(a, ' groupAnagrams result is ', result)

