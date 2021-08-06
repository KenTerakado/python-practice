def isLegalTriangle(s1,s2,s3):
    if (s1 <= 0 or s2 <= 0 or s3 <= 0): return False
    if ((s1**2 + s2**2) == (s3**2)): return True
    if ((s1**2 + s3**2) == (s2**2)): return True
    if ((s2**2 + s3**2) == (s1**2)): return True
    else: return False
    
def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert(isLegalTriangle(3, 4, 5) == True)
    assert(isLegalTriangle(5, 4, 3) == True)
    assert(isLegalTriangle(3, 5, 4) == True)
    assert(isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert(isLegalTriangle(3, 4, 7) == False)
    assert(isLegalTriangle(7, 4, 3) == False)
    assert(isLegalTriangle(3, 7, 4) == False)
    assert(isLegalTriangle(5, -3, 1) == False)
    assert(isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')
    
testIsLegalTriangle