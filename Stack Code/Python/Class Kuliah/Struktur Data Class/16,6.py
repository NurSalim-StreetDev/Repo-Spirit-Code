# Stack = ['UNIMAL','Fakultas Tehknik'];
# print('Stack Awal:',Stack)
# Stack.append('Prodi SI')
# Stack.append('Jurusan Elektro')
# print('\nStack setelah di tambahkan:',Stack)
# Stack.pop() 



# from collections import deque

# queue = deque(['UNIMAL','Fakultas Tekhnik']);
# print('queue awal :',queue)
# queue.append('Prodi SI')
# queue.append('Jurusan Elektro')
# print('\n queue setelah di tambahkan : ',queue)
# queue,popleft()
# print('queue setelah elemn pertama di hapus',queue)



# def SequenSearch(alist,item):
#     pos = 0
#     found = False
#     while pos < len (alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found

# testlist = [1,2,32,42,16,4,6,43,4,56,90]
# print('cari nilai 3 :',SequenSearch(testlist,3))
# print('cari nilai 42 :', SequenSearch(testlist,42))



def BinSearc(alist,item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            first = midpoint + 1
    return found

testlist = [0,12,8,13,17,19,32,42]
print('Cari nilai 3 :',BinSearc(testlist,3))
print('Cari nilai 42 :',BinSearc(testlist,42))
