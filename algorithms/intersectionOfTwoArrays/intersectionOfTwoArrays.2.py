# Source : https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Author : Ping Zhen
# Date   : 2017-04-12

'''*************************************************************************************** 
 *
 * Given two arrays, write a function to compute their intersection.
 * 
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
 * 
 * Note:
 * Each element in the result should appear as many times as it shows in both arrays.
 * The result can be in any order.
 * 
 * Follow up:
 * What if the given array is already sorted? How would you optimize your algorithm?
 * What if nums1's size is small compared to num2's size? Which algorithm is better?
 * What if elements of nums2 are stored on disk, and the memory is limited such that you
 * cannot load all elements into the memory at once?
 * 
 ***************************************************************************************'''
 
 '''* Solution
  * --------
  *
  * Follow up:
  * 
  * 1)If the given array is already sorted we can skip the sorting.
  * 
  * 2)If nums1 is significantly smaller than nums2 we can only sort nums1 and then binary
  * search every element of nums2 in nums1 with a total complexity of (MlogN) or if nums2
  * is already sorted we can search every element of nums1 in nums2 in O(NlogM)
  *
  * 3)Just like 2), we can search for every element in nums2, thus having an online
  * algorithm.
'''