def singleNumber(nums):
    visited_nums =  {}

    for num in nums:
        if num in visited_nums:
            del visited_nums[num]
        else:
            visited_nums[num] = True

    only_one = list(visited_nums.keys())[0]

    return only_one

nums = [-5,5,-4,-4,2,2,5]
sol = singleNumber(nums)
print(sol)