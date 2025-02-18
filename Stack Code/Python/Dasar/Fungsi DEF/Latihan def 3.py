# '''
# Mari kita membuat sesuatu yang luarbiasa
# '''
# # cara 1 pakai sum
# def list (item):
#     hasil = sum(item)
#     return hasil

# a = [1,2,3,4,5]
# print (list (a))

# # cara 2 pakai kondisi if
# # penjumlahan
# def sum_numbers(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + sum_numbers(numbers[1:])

# a = [1,2,3,4,5]
# print (sum_numbers([1, 2, 3, 4, 5]))

# def sum_numbers(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] - sum_numbers(numbers[1:])

# a = [1,2,3,4,5]
# print ('pengurangan',sum_numbers([1, 2, 3, 4, 5]))

# def sum_numbers(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] * sum_numbers(numbers[1:])

# a = [1,2,3,4,5]
# print (sum_numbers([1, 2, 3, 4, 5]))


# # memnggunakan loop
# penjumlahan
def penjumlahan (item):
    total = 0
    for item in item:
        total += item
    return total
total = 5
a = [1,2,3,4,5,5]
print (penjumlahan (a) )



# # pengurangan
# def pengurangan (item):
#     total = 4
#     for item in item:
#         total -= item
#     return total 

# a = [8,5]
# print  ('pengurangan', pengurangan (a) )


# #perkalian
# def perkalian (item):
#     total = 1
#     for item in item:
#         total *= item
#     return total

# a = [6,2,3,4,5,67]
# print  (perkalian (a) )

'''
membalikan string
'''
def balik_str (item):
    hasil = item[::-1]
    return hasil

a =str(input('Masukan kalimat\t:'))
print (balik_str (a))


# def data (b):
#     if b in a:
#         print ('Data anda ditemukan')
#     else:
#         print ('Maaf data anda tidak ditemukan')
#     return a
# a = [1,2,3,4,5]
# data (3)

