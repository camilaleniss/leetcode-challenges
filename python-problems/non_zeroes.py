def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        zeroes = []

        for index in range(0, len(nums)):
            if nums[index] == 0:
                zeroes.append(index)

        for index in range(0, len(zeroes)):
            nums.pop(zeroes[index]-index)
            nums.append(0)

        return nums

nums = [1, 2, 3]
print(moveZeroes(nums))