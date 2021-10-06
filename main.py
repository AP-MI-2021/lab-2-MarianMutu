""" preoblema 6
Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
"""
def is_superprime(n):
    """
    functia returneaza true daca n este superprim, false in caz contrar
    :return: true or false
    """
    while n>0:
        for d in range(2, n//2+1):
            if n % d == 0:
                return False
        n = n // 10
    return True


def test_is_superprime():
    """testam functia 'is_superpime' """
    assert is_superprime(237) == False
    assert  is_superprime(233) == True
    assert is_superprime(12) == False
    assert is_superprime(113) == True


"""problema 9
Transformă un număr dat din baza 2 în baza 16"""
def get_base_16(n):
    """calculam clase de resturi modulo 16"""
    power2=1
    base2=0
    while n > 0:
        base2 = n % 10 * power2 + base2
        power2 =power2 * 2
        n = n // 10
    return base2


def get_base_16_from_2(n: str):
    """trecem nr din baza 2 in baza 16, ajutandu-ne de functia 'get_base_16()' """
    rezultat="" #variabila in care se va afla rezultatul cerut
    var = int(n)
    sir = ["A","B","C","D","E","F"]
    while var:
        x = var % 10000
        nr = get_base_16(x)
        if nr >= 10:
           cifra=sir[nr-10]
        else:
            cifra=str(nr)
        rezultat = cifra + rezultat
        var = var // 10000
    return rezultat






def test_get_base_16_from_2():
    assert get_base_16_from_2(10101010) == 'AA'
    assert get_base_16_from_2(100111) == '27'
    assert get_base_16_from_2(11111) == '1F'




def main():
    test_is_superprime()
    test_get_base_16_from_2()
    while True:
        print("1.verifica daca un nr dat este superprim")
        print("2.calculam numarul in baza 16 din baza 2")
        print("3.iesire")

        optiune=input("alegeti o optiune:")

        if optiune == "1":
            numar1=int(input("introduceti numar:"))
            print(is_superprime(numar1))
        elif optiune == "2":
            numar2=int(input("introduceti numar:"))
            print(get_base_16_from_2(numar2))
        elif optiune == "3":
            break

        else:
            print("optiune gresita")

main()