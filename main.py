"""
preoblema 6
Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
Funcția principală: is_superprime(n) -> bool
Funcția de test: test_is_superprime()
problema 5
Determină dacă un număr dat este palindrom.
Funcția principală: is_palindrome(n) -> bool
Funcția de test: test_is_palindrome()
problema 9
Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2.
Funcția principală: get_base_16_from_2(n: str) -> str
Funcția de test: test_get_base_16_from_2()
"""


def is_superprime(n):
    """
    functia returneaza true daca n este superprim, false in caz contrar
    :return: true or false
    """
    while n > 0:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
        n = n // 10
    return True


def test_is_superprime():
    """testam functia 'is_superpime' """
    assert is_superprime(237) == False
    assert is_superprime(233) == True
    assert is_superprime(12) == False
    assert is_superprime(113) == True


"""problema 9
Transformă un număr dat din baza 2 în baza 16"""


def get_base_16(n):
    """calculam clase de resturi modulo 16"""

    power2 = 1
    base10 = 0
    while n > 0:
        base10 = n % 10 * power2 + base10
        power2 = power2 * 2
        n = n // 10
    return base10


def get_base_16_from_2(n: str):
    """trecem nr din baza 2 in baza 16, ajutandu-ne de functia 'get_base_16()' """
    rezultat = ""  # variabila in care se va afla rezultatul cerut
    var = int(n)  # variabila
    sir = ["A", "B", "C", "D", "E", "F"]
    while var:
        x = var % 10000  # grupam numarul in cate 4 cifre
        nr = get_base_16(x)
        if nr >= 10:  # prin conventie daca restul este mai mare decat 10 se noteaza cu litere (10=A, 11=B...)
            cifra = sir[nr - 10]
        else:
            cifra = str(nr)
        rezultat = cifra + rezultat
        var = var // 10000
    return rezultat


def test_get_base_16_from_2():
    assert get_base_16_from_2(str(10101010)) == 'AA'
    assert get_base_16_from_2(str(100111)) == '27'
    assert get_base_16_from_2(str(11111)) == '1F'


def is_palindrome(n):
    """
    verificam daca un nr dat este palindrom
    :param n: int
    :return: true or false
    """
    var = str(n)
    var = var[::-1]
    var = int(var)
    if var == n:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(12021) == True
    assert is_palindrome(122) == False
    assert is_palindrome(1) == True



def main():
    test_is_superprime()
    test_get_base_16_from_2()
    test_is_palindrome()
    while True:
        print("1.verifica daca un nr dat este superprim")
        print("2.calculam numarul in baza 16 din baza 2")
        print("3.verifica daca un nr dat este palindrom")
        print("4.iesire")


        optiune = input("alegeti o optiune:")

        if optiune == "1":
            numar1 = int(input("introduceti numar:"))
            print(is_superprime(numar1))
        elif optiune == "2":
            numar2 = str(input("introduceti numar:"))
            print(get_base_16_from_2(numar2))
        elif optiune == "3":
            numar3= int(input("introduceti numar:"))
            print(is_palindrome(numar3))
        elif optiune == "4":
            break

        else:
            print("optiune gresita")


main()
