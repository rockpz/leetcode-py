# Source : https://oj.leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
# Author : Ping Zhen
# Date   : 2017-04-17


'''
 * The API: int read4(char *buf) reads 4 characters at a time from a file.
 * 
 * The return value is the actual number of characters read. 
 * For example, it returns 3 if there is only 3 characters left in the file.
 * 
 * By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
 * 
 * Note:
 * The read function may be called multiple times.
'''


'''
 *  The key to solve this problem is: 
 *
 *    You have to buffer the extra data return from `read4()` API, which is for next call for `read()` .
'''