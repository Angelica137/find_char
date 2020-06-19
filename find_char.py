def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    midChar = aStr[len(aStr)//2]
    if char == midChar:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < midChar:
            return isIn(char, aStr[:len(aStr)//2])
        elif char > midChar:
            return isIn(char, aStr[len(aStr)//2:])


aStr = ''
char = 'b'

print(isIn(char, aStr))
