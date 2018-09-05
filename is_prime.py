import nose.tools as ns
"""
Vi skal her lage en funksjon som tester om et positivt heltall er et primtall.
Programmet skal fungere slik at det kræsjer dersom inputtet er feil.
"""


def is_prime(n):
    if not(isinstance(n, int)):
        raise TypeError("Input needs to be an integer.")
    if not(n > 0):
        raise ValueError("Input needs to be a positive number.")
    if n in (1, 2): return True
    for i in range(2,n):
        if not(n % i):
            return False
        else:
            return True

"""
Så skal vi lage noen tester!
"""

def test_is_prime():
    assert is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not(is_prime(6))
    assert not(is_prime(88))

@ns.raises (ValueError)
def testraisesValue_is_prime():
    is_prime(-5)

@ns.raises (TypeError)
def testraisesType_is_prime():
    is_prime("Jeg gikk en tur på stien og søkte skogens ro.")

if __name__ == "__main__":
    test_is_prime()
    testraisesValue_is_prime()
    testraisesType_is_prime()
