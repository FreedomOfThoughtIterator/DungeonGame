#Variables
RNGSeed = 0

def RNG():
    global RNGSeed
    if RNGSeed == 22026:
        RNGSeed = 0

    A = BinaryListToInt(BinaryList(RNGSeed, 8)) << 1
    A = A ^ RNGSeed
    RNGSeed = A
    LastByte = BinaryList(RNGSeed, 8)
    FirstByte = BinaryList(RNGSeed, 0)[:8]
    RNGSeed = BinaryListToInt(LastByte + FirstByte)
    A = BinaryListToInt(BinaryList(A, 8)) << 1
    A = A ^ RNGSeed
    B = A >> 1
    B = B ^ int('1111111110000000', 2)

    if int(BinaryList(A, 15)[0]) == 0:
        if B == 43605:
            RNGSeed = 0
        else:
            RNGSeed = B ^ int('0001111111110100', 2)
    else:
        RNGSeed = B ^ int('1000000110000000', 2)

    return RNGSeed

def Range(a: int, b: int):
    ReturnList = []
    if a < b:
        while a < b + 1:
            ReturnList.append(a)
            a += 1
    else:
        while a > b:
            while a > b - 1:
                ReturnList.append(a)
                a -= 1
    return ReturnList

def BinaryList(value, limit):
    BinList = list(bin(value))

    #Get the Binary List, without the 0b at the start
    BufferList = BinList[2:]
    #Create a second buffer list (max size of 16)
    #This will serve to create a 16 bit binary list
    BufferList2 = ['0'] * ((16 - len(BufferList)) % 16)
    BufferList = BufferList2 + BufferList
    #Return the Buffer List, past the limit. e.g. a limit of  8 would return the last 8 bits, a limit of 7 would return the last 9 bits
    ReturnList = BufferList[limit:]

    return ReturnList

def BinaryListToInt(binaryList):
    #Return the binary list converted back to an Integer
    return int(
        ''.join(
            #Map all values in the Binary List to strings
            map(
                str, binaryList
            )
        ),
        #The base of the inputted numerical strings
        2)

def RNGFromRange(a: int, b: int = 0):
    if b == 0 or b < a:
        Buffer = a
        a = b
        b = Buffer
    ModValue = b - a
    RNGValue = RNG() % ModValue + a
    return RNGValue