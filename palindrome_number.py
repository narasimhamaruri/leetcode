class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0 or (x%10==0 and x!=0)):
            return False
        reversed_half=0
        while(x>reversed_half):
            reversed_half=reversed_half*10 + (x%10)
            x=x//10
        if(x==reversed_half or x== reversed_half//10):
            return True
        return False



"""
Explanation:
Edge Cases:

If x is negative, it cannot be a palindrome.

If x ends with 0 (and is not 0 itself), it cannot be a palindrome (e.g., 10, 100).

Reversing Half the Number:

We reverse the second half of the number and compare it with the first half.

For example:

For x = 1221, we reverse the second half to get 12 and compare it with the first half 12.

For x = 12321, we reverse the second half to get 123 and compare 12 with 123 // 10 = 12.

Termination Condition:

The loop stops when x becomes less than or equal to reversed_half.


Optimal Solution:
We can reverse half of the number and compare it with the other half. This avoids converting the number to a string, which would use extra space.

Time Complexity (TC):

O(log 10(n)): We process each digit in the number once.

Space Complexity (SC):
O(1): We use constant extra space.
"""