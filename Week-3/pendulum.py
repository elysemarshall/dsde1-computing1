import math #import maths module for pi

def period(L, g):
    '''Returns value of T with users inputs of L and g'''
    if g == 0:
        raise ValueError
    T = 2*math.pi*((L/g)**(1/2))
    if isinstance(L or g, (int, float)):
        return T
    else:
        raise TypeError
    if L < 0:
        raise ValueError
