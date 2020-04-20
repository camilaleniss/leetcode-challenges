def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (len(nums)==0): return -1

        pivotPoint = findPivotPoint(nums, 0, len(nums)-1)

        if pivotPoint == -1:
            return binarySearch(nums, 0, len(nums)-1, target)

        if(nums[pivotPoint]==target):
            return pivotPoint

        if(nums[0]<=target):
            return binarySearch(nums, 0, pivotPoint-1, target)
        return binarySearch(nums, pivotPoint+1, len(nums)-1, target)

def findPivotPoint(nums, init, finale):
    if (finale<init):
        return -1

    if(finale==init):
        return init

    middle = (init + finale) // 2

    if(middle<finale and nums[middle] > nums[middle+1]):
        return middle
    if(middle>init and nums[middle] < nums[middle-1]):
        return middle-1

    if nums[init]>=nums[middle]:
        return findPivotPoint(nums, init, middle-1)
    return findPivotPoint(nums, middle+1, finale)


def binarySearch(nums, init, finale, target):
    if (finale< init):
        return -1

    middle = (init + finale) // 2

    if (target == nums[middle]):
        return middle
    if (target > nums[middle]):
        return binarySearch(nums, middle+1, finale, target)
    return binarySearch(nums, init, middle-1, target)


nums = [5,7,8,9,4]
target = 4
print(search(nums, target))
