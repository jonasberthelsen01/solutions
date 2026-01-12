"""
Opgave "chessboard":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion chessboard, der accepterer 2 parametre.
Kald funktionen med argumenterne rows og cols.
I denne eksempel skal funktionen udskrive "A1 A2 A3 A4 A5 B1 B2 .... D4 D5".

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
cols = ["1", "2", "3", "4", "5", "6", "7", "8"]

def chess(rows, cols):
    chessboard = []
    for row in rows:
        for col in cols:
            combine = row + col


            chessboard.append(combine)
    return chessboard



print(chess(rows, cols))



