# t =int(input("Masukan Nominal:"))
# for i in range (1,t+1):
#     for j in range (1,t+1):
#         print (j*i, end='')
    

# kita akan refresh dikit ya

t=int(input('silahkan masukan nominal:'))
for i in range (t):
    print (('*' * (2*i+1)). center (t*2))
for i in reversed (range (t-1)):
    print (('*' * (2*i+1)). center (t*2))

print ()

for i in reversed (range (t-1)):
    print ((i*'*'))
