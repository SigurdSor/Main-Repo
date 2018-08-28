""" Her skal vi telle hvor mange det er av hver bokstav i en tekststreng."""

def lettercount(string):
    string = string.lower()
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count.update({i:1})

    return count
"""
print(lettercount("SigurdSorensen"))
"""
