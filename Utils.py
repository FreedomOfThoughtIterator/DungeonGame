from util import RNGFromRange
from util import Range

def RandomRangeInt(a: int, b: int):
    return RNGFromRange(a, b)

def Random():
    RNGValue = RNGFromRange(0, 10000)
    return RNGValue / 10000.0

def InclusiveRange(a: int, b: int):
    return Range(a, b)