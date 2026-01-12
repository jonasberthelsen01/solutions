"""
Opgave "multiply_numbers":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen multiply_numbers() sådan at den gør hvad der står i dens dokumentation.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def multiply_numbers(start, multiplier, upper_limit):
    test = start
    print (test)

    for x in range(upper_limit):
        test = test * multiplier
        if test > upper_limit:
            break
        print(test)

def multiply_numbers2(start, multiplier, upper_limit):
    test = start
    print (test)

    while test * multiplier <= upper_limit:
        test = test * multiplier
        print (test)
    """
    Beginning with the start value, this function prints the current value,
    then multiplies it with multiplier, prints the new current value etc.
    The function stops when the current value is greater than the upper limit"""
    pass



multiply_numbers(10, 2, 12345)
multiply_numbers2(10, 2, 12345)