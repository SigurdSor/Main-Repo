import nose.tools as ns
"""
Vi skal her lage et program som sorterer en lisete med boblemetoden.
Boblemetoden er som følger:
    1 - Start med det første elementet i listen og sammenlikn det med det neste.
        Dersom de ikke er i riktig rekkefølge, bytt dem om.

    2 - Se så på det andre og tredje elementet i lista.
        Dersom de ikke er i riktig rekkefølge, bytt dem om.

    3 - Fortsett ut lista.

    4 . Gjør dette like mange ganger som lista er lang.
"""

def bubble_sort(liste):
    "Sort a list or tuple using bubble method."
    assert isinstance(liste, (list, tuple))
    sorted = liste.copy()
    for i in sorted:
        for j in range(len(sorted)-1):
            if sorted[j] > sorted[j+1]:
                sorted[j+1], sorted[j] = sorted[j], sorted[j+1]
    return sorted


def test_bubble_sort():
    test1 = [1, 5, 2, 13, 8]
    test1_copy = test1.copy()
    assert bubble_sort(test1) == [1, 2, 5, 8, 13]
    assert test1 == test1_copy
    test2 = []
    assert bubble_sort(test2) == test2
    test3 = [1]
    assert bubble_sort(test3) == test3


@ns.raises(TypeError)
def testlistcontent_bubble_sort():
    test1 = ["a", "b", "hytte", 42, bubble_sort]
    bubble_sort(test1)

if __name__ == "__main__":
    test_bubble_sort()
    testlistcontent_bubble_sort()
