# Source : https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
# Author : Ping Zhen
# Date   : 2017-04-14

'''********************************************************************************** 
 * 
 * Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
 * find the area of largest rectangle in the histogram.
 * 
 *                    6          
 *                  +---+        
 *               5  |   |        
 *              +---+   |        
 *              |   |   |        
 *              |   |   |        
 *              |   |   |     3  
 *              |   |   |   +---+
 *        2     |   |   | 2 |   |
 *      +---+   |   |   +---+   |
 *      |   | 1 |   |   |   |   |
 *      |   +---+   |   |   |   |
 *      |   |   |   |   |   |   |
 *      +---+---+---+---+---+---+
 *      
 * Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
 *      
 *      
 *                    6          
 *                  +---+        
 *               5  |   |        
 *              +-------|        
 *              |-------|        
 *              |-------|        
 *              |-------|     3  
 *              |-------|   +---+
 *        2     |-------| 2 |   |
 *      +---+   |-------|---+   |
 *      |   | 1 |-------|   |   |
 *      |   +---|-------|   |   |
 *      |   |   |-------|   |   |
 *      +---+---+---+---+---+---+
 *      
 * 
 * The largest rectangle is shown in the shaded area, which has area = 10 unit.
 * 
 * For example,
 * Given height = [2,1,5,6,2,3],
 * return 10.
 * 
 *               
 **********************************************************************************'''