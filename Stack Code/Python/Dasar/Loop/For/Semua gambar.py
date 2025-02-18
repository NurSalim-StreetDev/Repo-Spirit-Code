# # t =int(input('Masukan Nominal:'))
# # for i in range (1, t+1):
# #     print (i * '*')

# # t =int(input('Masukan Nominal:'))
# # for i in range (1, t+1):
# #     print ((t-i+1) * '*')

# # t =int(input('Masukan Nominal:'))
# # for i in range (1, t+1):
# #     print (((t-i+1) * ' ') + (i* '*'))

# # t =int(input('Masukan Nominal:'))
# # for i in range (1, t+1):
# #     print ((i * ' ') +((t-i+1) * '*'))

# # t =int(input('Masukan Nominal:'))
# # for i in range (1, t+1):
# #     print ((i * ' ') + (2*(t-i) * "*"))

# # t =int(input('Masukan Nomjnal:'))
# # for i in range (t):
# #     print (i+1)

# # t =int(input('Masukan Nominal:'))
# # for i in range (t+1):
# #     print ((t-i) * '6')

# # kita akan buat yang lebih sulit
# t =int(input('Masukan tinggi:'))
# for i in range (1,t+1):
#     print ()
#     for j in range (1, i+1):
#         print ('*', end='')
# for i in reversed (range(1,t)):
#     print ()
#     for j in range (1,i+1):
#         print ('*', end='')    


t=int(input('silahkan masukan nominal:'))
for i in range (t):
    print (( '*' * (1+2*i)).center (1+2*t))
for i in reversed (range (t-1)):
    print (( '*' * (1+2*i)).center (1+2*t))