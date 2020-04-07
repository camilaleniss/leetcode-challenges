def countElements(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    dict_elements = createDict(arr)

    count = 0

    for item in arr:
        if item+1 in dict_elements:
            count = count +1
    
    return count

def createDict(arr):
    dict_elements = {}

    for item in arr:
        if item in dict_elements:
            dict_elements[item].append(item)
        else:
            dict_elements[item] = []
            dict_elements[item].append(item)

    return dict_elements

arr =  [1,2,3]
print(countElements(arr))