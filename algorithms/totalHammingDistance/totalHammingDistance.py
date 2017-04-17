# Source : https://leetcode.com/problems/total-hamming-distance/
# Author : Ping Zhen
# Date   : 2017-04-17

'''*************************************************************************************** 
 *
 * The Hamming distance between two integers is the number of positions at which the 
 * corresponding bits are different.
 * 
 * Now your job is to find the total Hamming distance between all pairs of the given 
 * numbers.
 * 
 * Example:
 * Input: 4, 14, 2
 * 
 * Output: 6
 * 
 * Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
 * showing the four bits relevant in this case). So the answer will be:
 * HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
 * 
 * Note:
 * Elements of the given array are in the range of 0 to 10^9
 * Length of the array will not exceed 10^4.
 ***************************************************************************************'''

'''
*  Solution 1 - O(N)
*
* The total Hamming Distance is equal to the sum of all individual Hamming Distances
* between every 2 numbers. However, given that this depends on the individual bits of
* each number, we can see that we only need to compute the number of 1s and 0s for each
* bit position. For example, we look at the least significant bit. Given that we need to
* calculate the Hamming Distance for each pair of 2 numbers, we see that the answer is
* equal to the number of 1s at this position * the number of 0s(which is the total number
* of numbers - the number of 1s), because for each 1 we need to have a 0 to form a pair.
* Thus, the solution is the sum of all these distances at every position.
'''