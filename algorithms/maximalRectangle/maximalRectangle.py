# Source : https://oj.leetcode.com/problems/maximal-rectangle/
# Author : Ping Zhen
# Date   : 2017-04-14

'''********************************************************************************** 
* 
* Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
* containing all ones and return its area.
*               
**********************************************************************************'''

'''
 The problem can be convert to the problem - "Largest Rectangle in Histogram"
   1) we can take each row to calculate each row's histogram.
   2) using the algorithm of "Largest Rectangle in Histogram" to find the largest area histogram.
   3) tracking the maximal area.

 For the 1), it's easy. 
     heights[i][j] = 1,                     if (i==0)
     heights[i][j] = heights[i-1][j] + 1;,  if (i>0)

 For the 2), please referr to "Largest Rectangle in Histogram"
''' 