"""
Random numbers:

Inspicer følgende kode i detaljer. Find ud af, hvad hver række kode gør.
F.eks. ved at ændre koden en smule og derefter køre/debugge programmet.

Derefter går du videre med den næste fil. """


import random  # this imports a library called "random". A library is (someone else's) python code, that you can use in your own program.

# laver en linje per tal i range(), og giver så så mange linjer med et tal mellem 0 og 1
# makes a new line for each number in range(), and then makes that many lines with a random number between 0 and 1
for i in range(3):
    print(f"A random number between 0 and 1: {random.random()}")
print()


# laver en linje per tal i range(), og giver et integer tal (aka heltal) per linje i range(), mellem minimum og maximum
# makes a new line for each number in range(), for each line the code will give you a random integer (aka a counting number) between minimum and maximum which is defined below
minimum = 1
maximum = 5
for i in range(5):
    print(f"A random integer number between {minimum} and {maximum}: {random.randint(minimum, maximum)}")  #
print()

# laver en linje per tal i range(), laver et random tal per linje mellem 0 og 1, men gemmer disse tal under et "seed" så hvis man genbruger seeded for man de samme tal igen som første gang, i dette tilfælde er det seed 5
# makes a new line for each number in range(), creates a random number between 0 and 1 per line and saves them under a "seed", this means that every time you use the same seed you will get the same random number that you got the first time you used said seed in ths case the seed was 5
first_seed = 5
random.seed(first_seed)  # use seed() to create reproducible random numbers
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}")
print()

# laver en linje per tal i range(), laver et random tal per linje mellem 0 og 1, men gemmer disse tal under et "seed" så hvis man genbruger seeded for man de samme tal igen som første gang, i dette tilfælde er det seed 7
# makes a new line for each number in range(), creates a random number between 0 and 1 per line and saves them under a "seed", this means that every time you use the same seed you will get the same random number that you got the first time you used said seed in ths case the seed was 7
second_seed = 7  # another seed
random.seed(second_seed)
for i in range(3):
    print(f"A random number between 0 and 1 with seed {second_seed}: {random.random()}")
print()

# kalder det første seed igen, så man får tallende fra koden med first_seed
# calls the first seed again, so you get the same number as the code with the first_seed
random.seed(first_seed)  # same seed from before
for i in range(3):
    print(f"A random number between 0 and 1 with seed {first_seed}: {random.random()}")  # using the first seed again still creates the same random numbers
print()

# laver en linje per tal i range(), laver et random tal melem 0 og max_number (8 i dette tilfælde), max_number er også et "seed" så ver gang du kører koden med det samme max_number får du samme svar
# makes a new line for each number in range(), creates a random number between 0 and max_number (in this case 8), but this time max_number is also a seed which means that every time you use the same max_number, you will get the same set of numbers as the other times you've used that max_number
max_number = 8
for i in range(3):
    print(f"A random number between 0 and {max_number}: {random.random()*max_number}")
