
# #CONTOH LOGIKA SEDERHANA
# print ("*")
# print ("**")
# print ("***")
# print ("****")
# print ("*****")

# #INI ADALAH LOGIKA PERKALIAN
# print (5 * ("*"))

#MARI KITA COBA LEBIH COMPLEX
t =int(input("Masukan Tinggi Segitiga yang Dinginkan!:"))
for i in range(t+1):
    print ((t-i)*" "+(2*i) * "*")
else:
    print ("Mohon Ulangi")

#AYO KITA COBA HAL ANEH

t=int(input("masukan nominals:"))
for i in range (t+1):
    print ((2*i-1) * ("*"))

