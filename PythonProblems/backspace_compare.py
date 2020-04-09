def backspaceCompare(S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        cadena1 = convertString(S)
        cadena2 = convertString(T)
        return cadena1 == cadena2

def convertString(cadena):
    new_list = []
    for char in cadena:
        if char != "#":
            new_list.append(char)
        else:
            if (len(new_list)>0):
                new_list.pop()

    new_string = ""

    for item in new_list:
        new_string = new_string + item

    return new_string

print(backspaceCompare("a##c", "#a#c"))