def count_ones(left, right):
    # Your code here!
    """ 
    1 = 1       1

    2 = 10      1   
    3 = 11      2   4
        
    4 = 100     1
    5 = 101     2
    6 = 110     2
    7 = 111     3   8
    
    8 = 1000    1
    9 = 1001    2
    10= 1010    2
    11= 1011    3
    12= 1100    2
    13= 1101    3
    14= 1110    3
    15= 1111    4   20
    
    16= 10000   1

    1	2^0	1xF
    2	2^1	2 poz   1xF	1xH 
    4	2^2	3 poz	1xF 	2xH 
    8	2^3	4 poz	1xF 	3xH 
    16 	2^4	5 poz	1xF 	4xH 
    32	2^5	6 poz	1xF 	5xH 
    64	2^6	7 poz	1xF 	6xH 


    X	2^N	N+1 POZ	1xF	NxH

    """
    def zakres():
        lista_poteg_2 = [0, 0]
        for i in range(right):
            potega_2 = 2**i

            if potega_2 < left:
                lista_poteg_2[1]=potega_2
                lista_poteg_2[0]=i
                continue
            elif potega_2 > right:
                lista_poteg_2.append(potega_2)
                lista_poteg_2.insert(1, i)
                break
            else:
                lista_poteg_2.append(potega_2)

        return lista_poteg_2

    lista_poteg = zakres()

    potega_start    =   lista_poteg[0]
    potega_start2   =   potega_start
    potega_stop     =   lista_poteg[1]

    lista_poteg.pop(0)
    lista_poteg.pop(0)
    if lista_poteg[0]==0:
        lista_poteg.pop(0)

    jedynki = 0
    for i in range(len(lista_poteg)-1):
        if lista_poteg[i] == 1:
            jedynki+=1
            potega_start += 1
        else:
            roznica = lista_poteg[i+1] - lista_poteg[i]

            dodaj =  1*roznica + (potega_start)*0.5*roznica
            jedynki += dodaj

        
            potega_start += 1



    starting_point1 = 2**potega_start2
    starting_point2 = 2**potega_stop
    x = True
    string = ''
    while x:
        for i in range(starting_point1, left):
            string += str(bin(i))
        x = False
    liczba_minus = string.count('1')
    jedynki -= liczba_minus

    del liczba_minus

    x = True
    string = ''
    while x:
        for i in range(right+1, starting_point2):
            string += str(bin(i))
        x = False

    liczba_minus = string.count('1')

    jedynki -= liczba_minus
    
    return jedynki

#do 15 jest 32 jedynki

count_ones(3, 16)

"""

def count_ones(left, right):
    # Your code here!
    
    1 = 1       1   1

    2 = 10      1   
    3 = 11      2   3
        
    4 = 100     1
    5 = 101     2
    6 = 110     2
    7 = 111     3   8
    
    8 = 1000    1
    9 = 1001    2
    10= 1010    2
    11= 1011    3
    12= 1100    2
    13= 1101    3
    14= 1110    3
    15= 1111    4   20
    
    16= 10000   1

    1	2^0	1xF
    2	2^1	2 poz   1xF	1xH 
    4	2^2	3 poz	1xF 	2xH 
    8	2^3	4 poz	1xF 	3xH 
    16 	2^4	5 poz	1xF 	4xH 
    32	2^5	6 poz	1xF 	5xH 
    64	2^6	7 poz	1xF 	6xH 


    X	2^N	N+1 POZ	1xF	NxH

    

    def zakres():
        potegi_2 = {}
        for i in range(right):
            potega_2 = 2**i
            potegi_2[i] = potega_2
            if potega_2 >= right:

                break

        
            
        return potegi_2
    
    potegii_2 = zakres()
    
    
    


count_ones(9, 129)
"""