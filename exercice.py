#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if (number < 0):
        number = (-1)*number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for l in prefixes:
        stringFinale = ''.join((l,suffixe))
        liste.append(stringFinale)
    return liste


def prime_integer_summation() -> int:
    sum = 0
    nbrPrime = 0
    x=2
    while nbrPrime < 100:
        isPrime = True
        for i in range (2, x-1):
            if x%i == 0:
                isPrime = False
                break
        if isPrime:
            sum+=x
            nbrPrime+=1
        x+=1
    return sum


def factorial(number: int) -> int:
    factorielle = number
    while number>1:
        number-=1
        factorielle = factorielle*(number)
    return factorielle


def use_continue() -> None:
    for x in range(1,11):
        if x == 5:
            continue
        print(x)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    listeAcceptance = []
    for group in groups:
        isValid = True
        above70 = False
        exac50 = False
        exac25 = False

        for member in group:
            if member == 25:
                isValid = True
                exac25 = True
                break
            elif member < 18:
                isValid = False
            elif member > 70:
                above70 = True
            elif member == 50:
                exac50 = True

        if above70 and exac50 and not exac25:
            isValid = False

        if len(group) > 10 or len(group) <= 3:
            isValid = False

        if isValid:
            listeAcceptance.append(True)
        else:
            listeAcceptance.append(False)
    return listeAcceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
