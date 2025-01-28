class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        for i in range(len(nums)):
            other_num=target-nums[i]
            if(other_num in hm):
                return [hm[other_num],i]
            else:
                hm[nums[i]]=i
        

# TC- O(N)
# SC- O(N)


""""
Best Time Complexity (TC) and Space Complexity (SC):
1. Brute Force Approach:
Time Complexity: 
O(n2)

Space Complexity: 
O(1)


Explanation: Use two nested loops to check every pair of numbers.

2. Sorting and Two-Pointer Approach:
Time Complexity: 
O(nlogn)


Space Complexity: 

O(n) (if you need to store the original indices)

Explanation: Sort the array and use two pointers to find the pair. However, sorting changes the indices, so you need to store the original indices.

3. Hash Map (Optimal Solution):
Time Complexity: 
O(n)

Space Complexity: 
O(n)


Explanation: Use a hash map to store the difference between the target and the current number as you iterate through the array. This allows you to check for the required pair in constant time.


"""