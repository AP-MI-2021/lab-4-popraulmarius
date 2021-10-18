def prim(x):
    #determina daca un numar este prim
    if x<2:
        return 0
    if x==2:
        return 1
    for i in range (2,int(x/2)+1):
        if x%i==0:
            return 0
    return 1

def test_prim():
    assert prim(0)==0
    assert prim(2)==1
    assert prim(18)==0
    assert prim(-6)==0
    assert prim(17)==1

def div_proprii (x):
    #determina numarul de divizori proprii a unui numar intreg
    if x<=2:
        return 0
    nr_div=0
    for i in range (2,x//2+1):
        if x%i==0:
            nr_div+=1
    return nr_div

def test_div_proprii():
    assert div_proprii(1)==0
    assert div_proprii(2)==0
    assert div_proprii(17)==0
    assert div_proprii(4)==1


def medie_aritmetica(lst,n):
    #determina daca media aritmetica a numerelor din lista este mai mare sau nu decat un numar dat n
    suma=0
    for i in lst:
        suma+=i
    if suma/len(lst)>n:
        return "DA"
    else:
        return "NU"

def test_medie_aritmetica():
    assert medie_aritmetica([10, -3, 25, -1, 3, 25, 18],10)=="DA"
    assert medie_aritmetica([10,10,10],10)=="NU"
    assert medie_aritmetica([10,11],10)=="DA"
    assert medie_aritmetica([9,10],10)=="NU"

def elimina_nr_prime(lst):
    #elimina numerele prime din lista
    numere_prime_din_lst=[]
    for i in lst:
        if prim(i):
            numere_prime_din_lst.append(i)
    for i in numere_prime_din_lst:
        lst.remove(i)
    return lst

def test_elimina_nr_prime():
    assert elimina_nr_prime([8, 19, 17, 25])==[8, 25]
    assert elimina_nr_prime([1,0,2,17,100,56,13])==[1,0,100,56]
    assert elimina_nr_prime([2,13,17])==[]
    assert elimina_nr_prime([-7,7,0,2])==[-7,0]


def adaugare_div_proprii(lst):
    #adauga divizorii proprii dupa fiecare element din lista
    pozitie=0
    for i in range (0,2*len(lst),2):
        lst.insert(pozitie+1,div_proprii(lst[i]))
        pozitie+=2
    return lst


def test_adaugare_div_proprii():
    assert adaugare_div_proprii([19, 5, 24, 12, 9])==[19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert adaugare_div_proprii([2,0,4])==[2,0,0,0,4,1]
    assert adaugare_div_proprii([5,1,10])==[5,0,1,0,10,2]


def afisare_lista_tuplu(lst):
    #returneaza o lista de tupluri formate din fiecare element din lista impreuna cu indicele sau si cu numarul de aparitii
    lst2=[]
    pozitie=-1
    for i in lst:
        pozitie+=1
        numar_aparitii=0
        for j in lst:
            if i==j:
                numar_aparitii+=1
        lst2.append((i,pozitie,numar_aparitii))
    return lst2


def test_afisare_lista_tuplu():
    assert afisare_lista_tuplu([25,13,26,13])==[(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert afisare_lista_tuplu([10,10])==[(10,0,2),(10,1,2)]
    assert afisare_lista_tuplu([10,15,10])==[(10,0,2),(15,1,1),(10,2,2)]


def main():
    ok=1
    while True:
        if ok:
            m=input("Da lista de numere care doresti sa fie prelucrata, numerele trebuie sa fie separate prin spatiu:")
            lst2=(m.split(" "))
            map_object=map(int,lst2)
            lst=list(map_object)
            ok=0
        print ("0.Citeste alte numere.")
        print("1.Afiseaza lista dupa eliminarea numerelor prime.")
        print("2.Se va determina daca media aritmetica a numerelor din lista este mai mare sau nu decat un numar dat.")
        print("3.Adauga dupa fiecare element numarul de dizivori proprii ai acestuia.")
        print("4.Returneaza o lista de tupluri care contine elementul, indicele elementului si numarul de aparitii ale acestuia.")
        print("5.Iesire program.")
        optiune = input("Alege optiunea")
        if optiune=='0':
            m = input( "Da lista de numere care doresti sa fie prelucrata, numerele trebuie sa fie separate prin spatiu:")
            lst2 = (m.split(" "))
            map_object = map(int, lst2)
            lst = list(map_object)
        if optiune=='1':
            test_prim()
            test_elimina_nr_prime()
            print(elimina_nr_prime(lst))
        if optiune=='2':
            test_medie_aritmetica()
            n=int(input("Alege numarul cu care trebuie comparata media:"))
            print(medie_aritmetica(lst,n))
        if optiune=='3':
            test_div_proprii()
            test_adaugare_div_proprii()
            print(adaugare_div_proprii(lst))
        if optiune=='4':
            test_afisare_lista_tuplu()
            print(afisare_lista_tuplu(lst))
        if optiune=='5':
            break
main()

