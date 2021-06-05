import time
#
# def SortBombel(dane):
#     dl= len(dane)
#     for j in range(0,dl):
#         for i in range(0, dl -1):
#             if dane[i] > dane[i+1]:
#                 dane[i], dane[i+1] = dane[i+1], dane[i]
#     return dane
#
# def SortSelek(dane):
#     dl = len(dane)
#     i = 0
#     while i < dl - 1:
#         minI = i
#         j = i + 1
#         while j < dl:
#             if  dane[minI] > dane[j]:
#                 minI = j
#             j += 1
#         dane[i], dane[minI] = dane[minI], dane[i]
#         i += 1
#
#     return dane
#
#
# def SortWstawia(dane):
#     for i in range(1, len(dane)):
#         index = dane[i]
#         j = i - 1
#         while j >= 0 and dane[j] > index:
#             dane[j + 1] = dane[j]
#             j = j - 1
#         dane[j + 1] = index
#     return dane
#
plik = open("sort1.txt").readline().split()
dane = [int(ciag) for ciag in plik]
plik = open("sort2.txt").readline().split()
dane2 = [int(ciag) for ciag in plik]
plik = open("sort2.txt").readline().split()
dane3 = [int(ciag) for ciag in plik]

#start = time.time()
#dane1 = SortBombel(dane)
#stop = time.time()
#print(stop - start)

# start = time.time()
# dane1 = SortBombel(dane2)
# stop = time.time()
# print(stop - start)
#
# start = time.time()
# dane1 = SortBombel(dane3)
# stop = time.time()
# print(stop - start)
#
# start = time.time()
# dane1 = SortSelek(dane)
# stop = time.time()
# print(stop - start)
# start = time.time()
# dane1 = SortSelek(dane2)
# stop = time.time()
# print(stop - start)
# start = time.time()
# dane1 = SortSelek(dane3)
# stop = time.time()
# print(stop - start)
#
# start = time.time()
# dane1 = SortWstawia(dane)
# stop = time.time()
# print(stop - start)
# start = time.time()
# dane1 = SortWstawia(dane2)
# stop = time.time()
# print(stop - start)


def wyszukiwanie_binarne(dane, liczba):
    LB = 0
    UB = len(dane)-1

    while LB < UB:
        tmp = LB + (UB-LB+1)//2
        if tmp > liczba:
            UB = tmp - 1
        elif dane[tmp] < liczba:
            LB = tmp + 1
        else:
            return tmp
    return -1

start = time.time()
dane1 = dane
dane1.sort
stop = time.time()
print(stop - start)
print(dane1)

print(wyszukiwanie_binarne(dane1, 37))
mogę coś edytować  MCH