def tribonacci(signature, n):
    lista = signature
    i = 1
    while i < n:
        ble = lista[-1] + lista[-2] + lista[-3]
        lista.append(ble)
        print(lista)
        i += 1
        
    return lista

#the best solution on codewars ive found
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res


def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]



print(tribonacci([1, 1, 1], 10))# [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
print(tribonacci([0, 0, 1], 10))# [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
print(tribonacci([0, 1, 1], 10))# [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
print(tribonacci([1, 0, 0], 10))# [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
print(tribonacci([0, 0, 0], 10))# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(tribonacci([1, 2, 3], 10))# [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
print(tribonacci([3, 2, 1], 10))# [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])