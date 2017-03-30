# Source : https://leetcode.com/problems/add-and-search-word-data-structure-design/
# Author : Ping Zhen
# Date   : 2017-03-30

'''********************************************************************************** 
 * 
 * Design a data structure that supports the following two operations:
 * 
 * void addWord(word)
 * bool search(word)
 * 
 * search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`
 * A `.` means it can represent any one letter.
 * 
 * For example:
 * 
 *   addWord("bad")
 *   addWord("dad")
 *   addWord("mad")
 *   search("pad") -> false
 *   search("bad") -> true
 *   search(".ad") -> true
 *   search("b..") -> true
 * 
 * Note:
 * You may assume that all words are consist of lowercase letters a-z.
 * 
 * click to show hint.
 * 
 * You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
 * 
 *               
 **********************************************************************************'''

'''
trie，又称前缀树或字典树. 它利用字符串的公共前缀来节约存储空间.
性质：
根节点不包含字符，除根节点外的每个节点只包含一个字符
从根节点到某个节点，路径上经过的字符连接起来，为该节点对应的字符串
每个节点的所有子节点包含的字符串不相同

应用：
词频统计，比直接用hash节省空间
搜索提示，输入前缀的时候提示可以构成的词
作为辅助结构，Ac自动机等的辅助结构
'''

class TrieTree():
    def __init__(self):
        self.tree = {}

    def addWord(self, word):
        node = self.tree
        for char in word:
            node = node.setdefault(char, {})
        node['isWord'] = True
        print('cur Tree is ', self.tree)

    def search(self, word):
        return self.__getWord(word, self.tree)

    def __getWord(self, word, node):
        for i in range(0, len(word)):
            if(word[i] != '.'):
                if word[i] not in node:
                    return False
                else:
                    node = node[word[i]]
            else:
                for keys in node:
                    if not isinstance(node[keys], dict):
                        continue
                    if self.__getWord(word[i+1:], node[keys]):
                        return True
                return False

        return 'isWord' in node

if __name__ == '__main__':
    trieTree = TrieTree()
    trieTree.addWord('a')
    print(trieTree.search('.a'))
    print(trieTree.search('a.'))
    print(trieTree.search('a'))
    trieTree.addWord('abc')
    print(trieTree.search('.a'))
    print(trieTree.search('.b'))
    print(trieTree.search('.b.'))
    print(trieTree.search('abc'))
    print(trieTree.search('abcd'))







