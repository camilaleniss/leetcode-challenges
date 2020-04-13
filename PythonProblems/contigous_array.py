"""
def findMaxLength(nums):
    if len(nums)>1 :
        initindex = 0
        finaleindex = len(nums)-1
        return maximumSubarray(nums, initindex, finaleindex, 0, 0)
    else:
        return 0

def maximumSubarray(array, initindex, finaleindex, queue, lenght):
    if array[initindex] == 1 :
        queue = queue + 1
    else:
        queue = queue -1

    if initindex == finaleindex:
        if queue == 0:
            return lenght+1
        else:
            return 0

    middleindex = (initindex + finaleindex) // 2

    sum_left_subarray = maximumSubarray(array, initindex, middleindex, queue, lenght + 1)

    sum_right_subarray = maximumSubarray(array, middleindex+1, finaleindex, queue, lenght + 1)

    sum_middle_subarray = maximumMiddleSubarray(array, initindex, middleindex, finaleindex)

    return maxLength(sum_left_subarray, sum_right_subarray, sum_middle_subarray)

def maximumMiddleSubarray(array, initindex, middleindex, finaleindex):
    sum_left = 0
    lenght_left = 0

    for index in range(middleindex, initindex-1, -1):
        lenght_left = lenght_left + 1
        if array[index]== 1:
            sum_left = sum_left + 1
        else:
            sum_left = sum_left - 1 

    sum_right = 0
    lenght_right = 0

    for index in range(middleindex+1, finaleindex+1):
        lenght_right = lenght_right + 1
        if array[index]== 1:
            sum_right = sum_right + 1
        else:
         sum_right = sum_right - 1 

    if (sum_right == 0 and sum_left == 0) or (sum_left+sum_right==0): 
        return lenght_right+lenght_left
    elif sum_right == 0:
        return sum_right
    elif sum_left == 0:
        return sum_left
    return 0

    #Calcules the maximun number among 3 options
def maxLength(n1, n2, n3):
    if (n1>=n2 and n1>=n3):
        return n1
    elif (n2>=n1 and n2>=n3):
        return n2
    else:
        return n3

"""

def findMaxLength(nums):
    if len(nums)>1 :
        return findContigousSubarray(nums)
    else:
        return 0

def findContigousSubarray(nums):

    dict_visited_sum = {}
    length_array = len(nums)
    sum = 0
    max_length=0

    for index in range(0, length_array):
        if nums[index]==1:
            sum = sum + 1
        else:
            sum = sum - 1

        #Here the number of 1's is equal to the numbers of 2's
        if sum == 0:
            max_length = index + 1

        if (length_array + sum) in dict_visited_sum:
            if max_length < index - dict_visited_sum[length_array + sum]:
                max_length = index - dict_visited_sum[length_array + sum]
        else:
            dict_visited_sum[length_array + sum] = index

    return max_length
        
array = [1,0,1,0,1,0,0,0]
print(findMaxLength(array))