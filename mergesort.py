class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # make two arrays to search through the left and right
        left = []
        right = [] 
       
        if len(nums) > 1: # check to see if we're not dividing an empty array
            middle = len(nums)//2 # gets the middle of the array so that we can split in half
            left = nums[:middle] # first half goes to the left
            right = nums[middle:] # second half goes to the right
            # repeats the process until there's only one element in the array
            self.sortColors(left) 
            self.sortColors(right)

        # initialize pointers
        i = j = k = 0

        # while the arrays aren't empty
        while i < len(left) and j < len(right):
            # checks which side is smaller
            if left[i] < right[j]: 
                nums[k] = left[i] # adds to main array
                i +=1 # moves to next pointer
            else: 
                nums[k] = right[j] # adds to main array
                j +=1 # moves to next pointer
            k += 1 # moves to next spot in the main nums array
        
        while i < len(left): # checks left side 
            nums[k] = left[i]
            i+=1
            k+=1
            
        while j < len(right): # checks right side
            nums[k] = right[j]
            j+=1
            k+=1

