# Source : https://leetcode.com/problems/bulb-switcher/
# Author : Ping Zhen
# Date   : 2017-04-06

'''*************************************************************************************** 
 *
 * There are n bulbs that are initially off. You first turn on all the bulbs. Then, you
 * turn off every second bulb. On the third round, you toggle every third bulb (turning
 * on if it's off or turning off if it's on). For the nth round, you only toggle the
 * last bulb. Find how many bulbs are on after n rounds.
 * 
 * Example:
 * 
 * Given n = 3. 
 * 
 * At first, the three bulbs are [off, off, off].
 * After first round, the three bulbs are [on, on, on].
 * After second round, the three bulbs are [on, off, on].
 * After third round, the three bulbs are [on, off, off]. 
 * 
 * So you should return 1, because there is only one bulb is on.
 * 
 ***************************************************************************************'''

 '''* Solution
  * --------
  *
  * We know, 
  *   - if a bulb can be switched to ON eventually, it must be switched by ODD times
  *   - Otherwise, if a bulb has been switched by EVEN times, it will be OFF eventually.
  * So, 
  *   - If bulb `i` ends up ON if and only if `i` has an ODD numbers of divisors.
  * And we know, 
  *   - the divisors come in pairs. for example: 
  *     12 - [1,12] [2,6] [3,4] [6,2] [12,1] (the 12th bulb would be switched by 1,2,3,4,6,12)
  *   - the pairs means almost all of the numbers are switched by EVEN times.
  *
  * But we have a special case - square numbers
  *   - A square number must have a divisors pair with same number. such as 4 - [2,2], 9 - [3,3]
  *   - So, a square number has a ODD numbers of divisors.
  *
  * At last, we figure out the solution is: 
  *    
  *    Count the number of the squre numbers!! 
  *'''