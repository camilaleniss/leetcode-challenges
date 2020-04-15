def stringShift(s, shift):
    """
    :type s: str
    :type shift: List[List[int]]
    :rtype: str
    """
    dict_shift = convertShiftsDict(shift)

    if dict_shift[0] > dict_shift[1]:
        dict_shift[0] = dict_shift[0] - dict_shift[1]
        dict_shift[1] = 0
    elif dict_shift[1] > dict_shift[0]:
        dict_shift[1] = dict_shift[1] - dict_shift[0]
        dict_shift[0] = 0
    else:
        return s

    s = performShiftLeft(s, dict_shift[0])
    s = performShiftRight(s, dict_shift[1])
    return s

def convertShiftsDict(shift):
    dict_shift = {}
    dict_shift[0] = 0
    dict_shift[1] = 0

    for item in shift:
        if item[0] == 0:
            dict_shift[0] = dict_shift[0] + item[1]
        else:
            dict_shift[1] = dict_shift[1] + item[1]
    
    return dict_shift

def performShiftLeft(s, times):
    list_chars = list(s)

    for index in range(0, times):
        char = list_chars.pop(0)
        list_chars.append(char)

    return convertToString(list_chars)

def performShiftRight(s, times):
    list_chars = list(s)

    for index in range(0, times):
        char = list_chars.pop()
        list_chars.insert(0, char)

    return convertToString(list_chars)

def convertToString(s_list):
    s=''
    for item in s_list:
        s = s + item
    return s


s = "abc"
shift = [[0,1],[1,2]]
#print(performShiftLeft(s, 2))
print(stringShift(s, shift))