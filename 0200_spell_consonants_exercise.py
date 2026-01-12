"""
Opgave "spell_consonants":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen spell_consonants() sådan at den gør hvad der står i dens dokumentation.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def spell_consonants(text, letter_limit):
    text = text[:letter_limit]
    text = text.replace("a", "")
    text = text.replace("e", "")
    text = text.replace("i", "")
    text = text.replace("o", "")
    text = text.replace("u", "")
    text = text.replace("y", "")
    print(text)


def spell_consonants2(text, letter_limit):
    text = text[:letter_limit]
    vowels = ["a", "e", "i", "o", "u", "y"]
    blank = ""
    for vowel in text:
        if vowel not in vowels:
            blank += vowel
    print(blank)
    """
    Spells/prints the first letter_limit letters of text.
    Prints only consonants and spaces (a, e, i, o, u, y do not get printed). """
    pass


spell_consonants("Hello world", 9)  # should print "Hll wr"
spell_consonants("I love Python", 10)  # should print "I lv Pt"

spell_consonants2("Hello world", 9)  # should print "Hll wr"
spell_consonants2("I love Python", 10)  # should print "I lv Pt"
