import nose.tools as ns
"""
Her får vi gitt en funksjon for å finne medianen som vi skal lage gode tester til,
og skrive om til å fungere bedre.

Den gitte koden er:
def median(data):
    "Returns the median of a dataset."
    data.sort()
    return data[len(data)//2]

print(median([11, 3, 1, 5, 3]))
"""

def median(data):
    """Returns the median of a dataset."""
    data.sort()
    return data[len(data)//2]

def test_median():
    test1 = [1]
    test2 = [-89, 56]
    test3 = test2.copy()
    test4 = [0, 0, 0, 0, 0]
    assert test1[0] == median(test1)
    assert test2[1] == median(test2)
    assert test2 == test3
    assert median(test4) == 0

@ns.raises(TypeError)
def testType_median():
    test1 = [1, "pølse", median]
    median(test1)

@ns.raises(IndexError)
def testIndex_median():
    test1 = []
    median(test1)


if __name__ == "__main__":
    test_median()
    testType_median()
    testIndex_median()
