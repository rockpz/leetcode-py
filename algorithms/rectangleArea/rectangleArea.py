# Source : https://leetcode.com/problems/rectangle-area/
# Author : Ping Zhen
# Date   : 2017-04-17

'''********************************************************************************** 
 * 
 * Find the total area covered by two rectilinear rectangles in a 2D plane.
 * Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
 * 
 *                      Y                                        
 *                      ^                                        
 *                      |                                        
 *                      |                                        
 *                      |                                        
 *                      |                                        
 *                      |     (C,D):(3,4)                        
 *            +------------------+                               
 *            |         |        |                               
 *            |         |        |                               
 *            |         |        |               (G,H):(9,2)     
 *            |         +----------------------------+           
 *            |         |        |                   |           
 *            |         |        |                   |           
 *            |         |        |                   |           
 *            +---------|--------+-------------------|---------> X
 *      (A,B):(-3,0)    |                            |           
 *                      +----------------------------+           
 *                  (E,F):(0,-1)                                 
 *      
 *      
 *      
 * Assume that the total area is never beyond the maximum possible value of int.
 * 
 * Credits:Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.
 *               
 **********************************************************************************'''