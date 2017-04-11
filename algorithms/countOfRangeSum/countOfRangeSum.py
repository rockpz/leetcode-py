# Source : https://leetcode.com/problems/count-of-range-sum/
# Author : Ping Zhen
# Date   : 2017-04-06

'''*************************************************************************************** 
 *
 * Given an integer array nums, return the number of range sums that lie in [lower, 
 * upper] inclusive.
 * 
 *     Range sum S(i, j) is defined as the sum of the elements in nums between indices 
 * i and 
 *     j (i ≤ j), inclusive.
 * 
 *     Note:
 *     A naive algorithm of O(n2) is trivial. You MUST do better than that.
 * 
 *     Example:
 *     Given nums = [-2, 5, -1], lower = -2, upper = 2,
 *     Return 3.
 *     The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
 * 
 * Credits:Special thanks to @dietpepsi for adding this problem and creating all test 
 * cases.
 *               
 ***************************************************************************************'''


'''
 *  At first of all, we can do preprocess to calculate the prefix sums 
 * 
 *      S[i] = S(0, i), then S(i, j) = S[j] - S[i]. 
 *  
 *  Note: S(i, j) as the sum of range [i, j) where j exclusive and j > i. 
 *
 *  With these prefix sums, it is trivial to see that with O(n^2) time we can find all S(i, j) 
 *  in the range [lower, upper]
 *
 *      int countRangeSum(vector<int>& nums, int lower, int upper) {
 *        int n = nums.size();
 *        long[] sums = new long[n + 1];
 *        for (int i = 0; i < n; ++i) {
 *            sums[i + 1] = sums[i] + nums[i];
 *        }
 *        int ans = 0;
 *        for (int i = 0; i < n; ++i) {
 *            for (int j = i + 1; j <= n; ++j) {
 *                if (sums[j] - sums[i] >= lower && sums[j] - sums[i] <= upper) {
 *                    ans++;
 *                }
 *            }
 *        }
 *        delete []sums;
 *        return ans;
 *      }
 * 
 *  The above solution would get time limit error.
 *
 *  Recall `count smaller number after self` where we encountered the problem
 *
 *      count[i] = count of nums[j] - nums[i] < 0 with j > i
 *
 *  Here, after we did the preprocess, we need to solve the problem
 *
 *      count[i] = count of a <= S[j] - S[i] <= b with j > i   
 *
 *  In other words, if we maintain the prefix sums sorted, and then are able to find out 
 *  - how many of the sums are less than 'lower', say num1, 
 *  - how many of the sums are less than 'upper + 1', say num2, 
 *  Then 'num2 - num1' is the number of sums that lie within the range of [lower, upper].
 *
 *'''