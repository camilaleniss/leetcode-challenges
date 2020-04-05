def maxSubArray(nums):
    if len(nums)>1 :
        initindex = 0
        finaleindex = len(nums)-1
        return maximumSubarray(nums, initindex, finaleindex)
    else:
        return nums[0]

#The maximun subarray could be in the left, in the right or somewhere in the middle
def maximumSubarray(array, initindex, finaleindex):
    if initindex == finaleindex:
        return array[finaleindex]

    middleindex = (initindex + finaleindex) // 2

    sum_left_subarray = maximumSubarray(array, initindex, middleindex)

    sum_right_subarray = maximumSubarray(array, middleindex+1, finaleindex)

    sum_middle_subarray = maximumMiddleSubarray(array, initindex, middleindex, finaleindex)

    return maxNumber(sum_left_subarray, sum_right_subarray, sum_middle_subarray)

INFINITY_NUMBER = -1000000

def maximumMiddleSubarray(array, initindex, middleindex, finaleindex):
    left_sum = INFINITY_NUMBER
    right_sum = INFINITY_NUMBER

    sum = 0

    for index in range(middleindex, initindex-1, -1):
        sum = sum + array[index]

        if (sum>left_sum):
            left_sum = sum

    sum = 0

    for index in range(middleindex+1, finaleindex+1):
        sum = sum + array[index]

        if (sum>right_sum):
            right_sum = sum

    return left_sum+right_sum

#Calcules the maximun number among 3 options
def maxNumber(n1, n2, n3):
    if (n1>=n2 and n1>=n3):
        return n1
    elif (n2>=n1 and n2>=n3):
        return n2
    else:
        return n3

array = [1,2,-1]
print(maxSubArray(array))
#The response sould be 3