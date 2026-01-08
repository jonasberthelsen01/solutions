"""
Opgave "square numbers":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv kode i funktionen, som printer alle kwadrattal (1, 4, 9, ...), som er mindre end limit.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def print_squarenumbers(limit):
    squares = [x * x for x in range(1, int(limit ** 0.5) + 1)]
    pass
    return squares

def print_squarenumbers2(limit):
    squares = []
    for x in range(limit + 1):
        x = x * x
        if x >= limit:
            return squares

        squares.append(x)



print (print_squarenumbers2(700))