def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums_length = len(nums)
    product_array = []
    product_array.append(1)

    for index in range(1, nums_length):
        product_array.append(product_array[index-1] * nums[index-1])

    carry = 1

    for index in range(nums_length-1, -1, -1):
        product_array[index] = product_array[index] * carry
        carry = nums[index] * carry

    return product_array


nums =[1,2,3,4]
print(productExceptSelf(nums))




        